package main

import (
	"fmt"
	"unsafe"
)

type Hehe struct {
	a []int
	b map[int]string
	c *int
	s *string
}

func main() {
	var a int = 10
	var b int16
	var c int64
	var d string = "kdsjflsdjfjfsdjfsdlf"
	h := Hehe{a: []int{1, 2, 3}, b: map[int]string{1: "lkjfls", 2: "lk"}, c: &a, s: &d}
	fmt.Println("Size of int", unsafe.Sizeof(a))
	fmt.Println("Size of int16", unsafe.Sizeof(b))
	fmt.Println("Size of int64", unsafe.Sizeof(c))
	fmt.Println("Size of h", unsafe.Sizeof(h))
	fmt.Printf("%v", h)
}
