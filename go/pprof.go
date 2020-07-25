package main

import (
	"fmt"
	"os"
	"runtime/trace"
	"time"
)

func main() {
	trace.Start(os.Stderr)
	defer trace.Stop()

	ch := make(chan string, 2)
	for i := 0; i < 100; i++ {
		go func() {
			for {
				select {
				case <-time.After(5 * time.Second):
					break
				case ch <- "value":

				}
				time.Sleep(20 * time.Millisecond)
			}
		}()
	}
	for i := 0; i < 10; i++ {
		go func() {
			for {
				select {
				case val, ok := <-ch:
					if ok {
						fmt.Println(val)
					} else {
						return
					}
				}
			}
		}()
	}
	time.Sleep(10 * time.Second)
}
