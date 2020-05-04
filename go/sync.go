package main

import (
	"context"
	"fmt"
	"sync"
	"time"
)

var mailbox uint8
var lock sync.RWMutex
var sendCond = sync.NewCond(&lock)
var recvCond = sync.NewCond(lock.RLocker())

func main() {
	ctx := context.Background()
	ctx, cancel := context.WithCancel(ctx)
	go func(ctx context.Context) {
		for {
			select {
			case <-ctx.Done():
				fmt.Println("exit in select 3")
				// 这里不可以写break，break的是这个select
				return
			case <-ctx.Done():
				fmt.Println("exit in select 4")
				return
			default:
				lock.Lock()
				for mailbox == 1 {
					sendCond.Wait()
				}
				mailbox = 1
				lock.Unlock()
				recvCond.Signal()
			}
		}
	}(ctx)

	go func(ctx context.Context) {
		for {
			select {
			case <-ctx.Done():
				fmt.Println("exit in select 1")
				return
			case <-ctx.Done():
				fmt.Println("exit in select 2")
				return
			default:
				lock.RLock()
				for mailbox == 0 {
					recvCond.Wait()
				}
				mailbox = 0
				lock.RUnlock()
				sendCond.Signal()
			}

		}
	}(ctx)

	fmt.Println("Start send recv msg")
	time.Sleep(10 * time.Second)
	cancel()
	fmt.Println("Send Recv msg is Done")
	time.Sleep(10 * time.Second)
}
