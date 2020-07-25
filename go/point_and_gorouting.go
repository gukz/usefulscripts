package main

import (
	"fmt"
	"time"
)

type field struct {
	val string
}

func (f *field) say() {
	// println(f, f.val)
	fmt.Printf("%p\n", f)
	fmt.Println(f, f.val)
}

func main() {
	// 循环内的v的只被定义一次，每次循环时值被修改。
	// 当v是指针类型时，v的值（field数组里的真实struct的指针）可以传进print函数，可以正常打印。
	// 当v是值类型时，go会把代码改写成&v.print 这样传进print的地址都是v的地址。v在循环结束前被改成了six这个值。
	a1 := []*field{{"one"}, {"two"}, {"three"}}
	for _, v := range a1 {
		fmt.Printf("%p\n", v)
		go v.say()
		time.Sleep(1 * time.Second)
	}
	time.Sleep(1 * time.Second)
	a2 := []field{{"four"}, {"five"}, {"six"}}
	for _, v := range a2 {
		fmt.Printf("%p\n", &v)
		go v.say()
		time.Sleep(1 * time.Second)
	}
	time.Sleep(1 * time.Second)
}
