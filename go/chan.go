package main

import (
	"fmt"
	"time"
)

func dupCloseChan() {
	ch1 := make(chan int, 1)
	var ch2 chan (int)

	// 重复关闭一个chan或者关闭一个为nil的chan引发的panic可以被recover
	// 运行环境 go1.14
	close(ch1)
	fmt.Println("close ch1 ok")
	close(ch1)
	fmt.Println("close ch1 ok")

	close(ch2)
	fmt.Println("close ch1 ok")
}

func commonRecover() {

	defer func() {
		err := recover()
		fmt.Println("%s", err)
	}()
	dupCloseChan()
}

func main() {
	commonRecover()
	for {
		time.Sleep(1 * time.Second)
		fmt.Println("main loop")

	}
}
