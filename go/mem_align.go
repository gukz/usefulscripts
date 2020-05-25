package main

import (
	"fmt"
	"unsafe"
)

type Hehe1 struct {
	a bool
	b int16
	c bool
}

type Hehe2 struct {
	a bool
	b bool
	c bool
}

type Hehe3 struct {
	h Hehe1
	a bool
	b int16
	c bool
}

func main() {

	h1 := Hehe1{}
	h2 := Hehe2{}
	h3 := Hehe3{}
	fmt.Println(unsafe.Sizeof(h1))
	fmt.Println(unsafe.Sizeof(h2))
	fmt.Println(unsafe.Sizeof(h3))

}
