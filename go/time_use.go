package main

import (
	"fmt"
	"time"
)

func main() {
	var t int64
	for {
		unixnow := time.Now().UnixNano()
		fmt.Println(unixnow - t)
		t = unixnow
	}

}
