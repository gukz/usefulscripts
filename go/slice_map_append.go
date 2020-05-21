package main

import (
	"fmt"
)

type Int int

func (i *Int) pprint() {
	fmt.Printf("%d, %p\n", *i, i)
}

func (i Int) print() {
	fmt.Printf("%d, %p\n", i, &i)
}

func addr_slice() {
	a := []Int{1, 2}
	for i, _ := range a {
		a[i].print()  // 值拷贝传参
		a[i].pprint() // 转指针后，拷贝指针传参
	}
}

func addr_map() {
	a := map[int]Int{1: 1, 2: 2}
	for k, _ := range a {
		a[k].print()
		// (a[k]).pprint() // 不允许，map无法取地址
	}
}

func append_slice(a []int) {

	a[0] = 10
	a = append(a, 4)

}

func main() {
	// addr_slice()
	// addr_map()

	a := []int{1, 2, 3}
	fmt.Println(a)
	append_slice(a)
	fmt.Println(a)
	b := map[int]*string{}
	c := "hello"
	b[1] = &c
	fmt.Println(b)
}
