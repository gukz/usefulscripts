package main

import (
	"encoding/binary"
	"errors"
	"fmt"
	"hash/crc32"
	"io/ioutil"
)

const (
	pngSign uint64 = 0x89504e470d0a1a0a // 文件头
	iHDR    uint32 = 0x49484452         // 起始块
	iDAT    uint32 = 0x49444154         // 数据块
	iEnd    uint32 = 0x49454e44         // 结尾块
)

type chunk struct {
	Length   uint32
	TypeCode uint32
	Data     []byte
	// CRC 校验和包含 TypeCode和Data
	CRC uint32
}

func (c *chunk) display() {
	fmt.Println("")
	switch c.TypeCode {
	case iHDR:
		fmt.Printf("Length:           %d\n", c.Length)
		fmt.Printf("Chunk Type Code:  %x(iHDR)\n", c.TypeCode)
		fmt.Printf("宽度: %d, 高度: %d\n", binary.BigEndian.Uint32(c.Data[0:4]), binary.BigEndian.Uint32(c.Data[4:8]))
		fmt.Printf("色深: %d色\n", c.Data[8])
		fmt.Printf("颜色类型: %d\n", c.Data[9])
		fmt.Printf("使用压缩: %t\n", c.Data[10] != 0)
		fmt.Printf("使用压缩: %t\n", c.Data[11] != 0)
		fmt.Printf("非隔行扫描: %t\n", c.Data[12] != 0)
	default:
		fmt.Printf("Length:           %d\n", c.Length)
		fmt.Printf("Chunk Type Code:  %x\n", c.TypeCode)
	}
}

func buildChunk(chunkType uint32, data []byte) *chunk {
	res := &chunk{
		Length:   uint32(len(data)),
		TypeCode: chunkType,
		Data:     data,
	}
	buf := make([]byte, 4)
	binary.BigEndian.PutUint32(buf, res.TypeCode)
	buf = append(buf, data...)
	res.CRC = crc32.ChecksumIEEE(buf)
	return res
}
func listAllChunks(data []byte) (res []*chunk) {
	if binary.BigEndian.Uint64(data[:8]) != pngSign {
		return
	}
	for offset := 8; offset < len(data); {
		// 读一个chunk
		length := int(binary.BigEndian.Uint32(data[offset : offset+4]))
		typeCode := binary.BigEndian.Uint32(data[offset+4 : offset+8])
		chunkData := data[offset+8 : offset+8+length]
		// validate crc
		crc := binary.BigEndian.Uint32(data[offset+8+length : offset+12+length])
		realCrc := crc32.ChecksumIEEE(data[offset+4 : offset+8+length])
		if crc != realCrc {
			panic(errors.New("crc check failed"))
		}
		offset = offset + 12 + length
		res = append(res, buildChunk(typeCode, chunkData))
	}
	return
}

func printHex(val []byte) {
	fmt.Printf("%x\n", val)
}

func main() {
	data, _ := ioutil.ReadFile("aaa.png")

	chunks := listAllChunks(data)
	for _, c := range chunks {
		c.display()
	}
}

/*
png图像格式由文件署名和数据块（chunk）组成
文件署名
数据块
参考：https://blog.mythsman.com/post/5d2d62b4a2005d74040ef7eb/
*/
func bytes2png(data []byte, pngPath string) bool {
	return false
}

func png2bytes(pngPath string) ([]byte, error) {
	return nil, nil
}
