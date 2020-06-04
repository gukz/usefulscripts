package main

import (
	"fmt"
	"sync"
)

func printNumber(ch_num chan struct{}, ch_char chan struct{}) {
	curNum := 1
	for {
		select {
		case _ = <-ch_num:
			fmt.Print(curNum)
			curNum += 1
			fmt.Print(curNum)
			curNum += 1
			ch_char <- struct{}{}
		}
	}
}

func printChar(wg *sync.WaitGroup, ch_num chan struct{}, ch_char chan struct{}) {
	defer wg.Done()
	curChar := 0
	chars := "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for {
		select {
		case _ = <-ch_char:
			fmt.Printf("%c", chars[curChar])
			curChar += 1
			fmt.Printf("%c", chars[curChar])
			curChar += 1
			ch_num <- struct{}{}
			if curChar >= len(chars) {
				return
			}
		}
	}
}

func main() {
	wg := &sync.WaitGroup{}
	ch_num := make(chan struct{})
	ch_char := make(chan struct{})
	wg.Add(1)
	go printNumber(ch_num, ch_char)
	go printChar(wg, ch_num, ch_char)
	ch_num <- struct{}{}
	wg.Wait()
}
