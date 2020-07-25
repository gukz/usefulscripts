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
	go_main()
	commonRecover()
	time.Sleep(1 * time.Second)
	fmt.Println("main loop")
	alwaysReadFromChan()
}

func go_main() {
	words := []string{"foo", "bar", "baz"}
	// Create a channel for communication
	done := make(chan bool)
	// It is nice to close the channels, like files,
	// after it's used or you may get leaks
	defer close(done)
	for _, w := range words {
		go func(word string) {
			// block for a sec
			time.Sleep(1 * time.Second)
			fmt.Println(word)

			// send signal to the channel
			done <- true
		}(w)
	}
	// Do what you have to do
	fmt.Println(1)
	time.Sleep(1 * time.Second)
	fmt.Println(2)
	time.Sleep(1 * time.Second)
	fmt.Println(3)
	// This blocks and waits
	<-done
}
