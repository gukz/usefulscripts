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

func alwaysReadFromChan() {
	ch := make(chan int, 5)
	vals := []int{1, 2, 3, 4, 5}
	for _, v := range vals {
		ch <- v
	}
	close(ch)
	c := 0
	for {
		select {
		case v, ok := <-ch:
			fmt.Println(v, ok)
			if !ok {
				goto END
			}
		default:
			c += 1
		}
		if c > 10 {
			break
		}
	}
END:
	fmt.Println(c)
}

func main() {
	commonRecover()
	time.Sleep(1 * time.Second)
	fmt.Println("main loop")
	alwaysReadFromChan()
}
