package main

import (
	"bytes"
	"encoding/binary"
	"fmt"
	"math"
)

func main() {
	var pi float64 = math.Pi
	buf := new(bytes.Buffer)
	binary.Write(buf, binary.LittleEndian, pi)
	fmt.Println(buf.Bytes())
}
