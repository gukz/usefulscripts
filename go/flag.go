package main

import (
	"flag"
	"fmt"
)

var (
	name   = flag.String("name", "anyone", "please input your name")
	age    = flag.Int("age", 16, "please input your age")
	height int
)

func init() {
	flag.IntVar(&height, "height", 170, "please tell me your height")
}

func main() {
	flag.Parse()

	fmt.Println(*name, *age, height)
}
