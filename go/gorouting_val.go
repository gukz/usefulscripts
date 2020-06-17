package main

import (
	"fmt"
	"time"
)

func main() {
	a := []int{1, 3, 5, 7, 9}
	for _, v := range a {
		val := v
		go func(x int) {
			time.Sleep(1 * time.Second)
			fmt.Println(val, x, v)
		}(v)
	}
	time.Sleep(10 * time.Second)
}
