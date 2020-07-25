package main

import (
	"bytes"
	"compress/bzip2"
	"compress/gzip"
	"fmt"
	// "encoding/json"
	"errors"
	// "git.17bdc.com/shanbay/protos-go/words"
	// "github.com/ulikunitz/xz"
	"github.com/ulikunitz/xz/lzma"
	"hash/crc32"
	"io"
)

type Compressor interface {
	Compress(data []byte, level int) []byte
	Decompress(data []byte) []byte
}

type Dummy struct {
}

func (d Dummy) Compress(data []byte, level int) []byte {
	return data
}
func (d Dummy) Decompress(data []byte) []byte {
	return data
}

func checkErr(err error) {
	if err != nil {
		panic(err)
	}
}

type Gzip struct {
}

func (g Gzip) Compress(data []byte, level int) []byte {
	var origin bytes.Buffer
	writer, err := gzip.NewWriterLevel(&origin, level)
	checkErr(err)
	_, err = writer.Write(data)
	checkErr(err)
	writer.Close()
	return origin.Bytes()
}
func (g Gzip) Decompress(data []byte) []byte {
	var origin bytes.Buffer
	_, err := origin.Write(data)
	checkErr(err)
	reader, err := gzip.NewReader(&origin)
	checkErr(err)
	var res bytes.Buffer
	_, err = io.Copy(&res, reader)
	checkErr(err)
	return res.Bytes()
}

type Lzma struct {
}

func (l Lzma) Compress(data []byte, level int) []byte {
	var buf bytes.Buffer
	writer, err := lzma.NewWriter2(&buf)
	checkErr(err)
	_, err = io.WriteString(writer, string(data))
	checkErr(err)
	checkErr(writer.Close())
	return buf.Bytes()
}

func (l Lzma) Decompress(data []byte) []byte {
	var res bytes.Buffer
	buf := bytes.NewBuffer(data)
	reader, err := lzma.NewReader2(buf)
	checkErr(err)
	_, err = io.Copy(&res, reader)
	checkErr(err)
	return res.Bytes()
}

type BZ2 struct {
}

func (b BZ2) Compress(data []byte, level int) []byte {
	panic(errors.New("Not support compress data to bz2"))
}
func (b BZ2) Decompress(data []byte) []byte {
	buf := bytes.NewBuffer(data)
	reader := bzip2.NewReader(buf)
	var res bytes.Buffer
	_, err := io.Copy(&res, reader)
	checkErr(err)
	return res.Bytes()
}

func GetChecksum(data []byte) uint32 {
	return crc32.ChecksumIEEE(data)
}

// type Serializer interface {
//     Serialize(*words.CompressedItems) []byte
//     Deserialize([]byte) *words.CompressedItems
// }
// type JsonItemsSerializer struct {
// }
//
// func (j JsonItemsSerializer) Serialize(data *words.CompressedItems) []byte {
//     byte_list, err := json.Marshal(data)
//     checkErr(err)
//     return byte_list
// }
//
// func (j JsonItemsSerializer) Deserialize(data []byte) *words.CompressedItems {
//     var res = &words.CompressedItems{}
//     checkErr(json.Unmarshal(data, &res))
//     return res
// }
//
// type ProtobufItemsSerializer struct{}
//
// func (j ProtobufItemsSerializer) Serialize(data *words.CompressedItems) []byte {
//     res, err := data.Marshal()
//     checkErr(err)
//     return res
// }
//
// func (j ProtobufItemsSerializer) Deserialize(data []byte) *words.CompressedItems {
//     res := &words.CompressedItems{}
//     checkErr(res.Unmarshal(data))
//     return res
// }

func main() {
	data := []byte("你好世界")
	fmt.Println("origin", data)
	c := Lzma{}
	compressData := c.Compress(data, 1)
	fmt.Println(compressData)
	fmt.Println(GetChecksum(compressData))
}
