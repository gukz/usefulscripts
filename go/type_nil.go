package main

import (
	"fmt"
)

type AAA nil

// nil (untyped nil value) is not a type
func (AAA) Hello() {
	fmt.Println("Hello")
}

func mian() {
	fmt.Println("hello")
}
