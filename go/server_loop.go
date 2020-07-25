package main

import (
	"fmt"
	"strconv"
	"sync"
	"time"
)

func main() {
	serve(9)
}

var data int64 = 1

func getMessage() string {
	if data > 100 && data < 150 {
		data += 10
		fmt.Println("try get message, but failed", data)
		time.Sleep(1 * time.Second)
		return ""
	}
	data += 1
	return "receive message: " + strconv.FormatInt(data, 10)
}

func workFunc(msg string) error {
	time.Sleep(1 * time.Second)
	fmt.Println(msg)
	return nil
}

func serve(concurrency int) {
	quitSignal := make(chan struct{})
	var wg sync.WaitGroup
	go func() {
		for {
			if data > 300 {
				quitSignal <- struct{}{}
			}
		}
	}()

	pool := make(chan struct{}, concurrency)
	for i := 0; i < concurrency; i++ {
		pool <- struct{}{}
	}
	for {
		select {
		case <-quitSignal:
			goto STOP
		default:
			<-pool
			wg.Add(1)
			go func() {
				defer wg.Done()
				workFunc(getMessage())
				pool <- struct{}{}
			}()
		}
	}
STOP:
	wg.Wait()
}
