package main

import (
	"fmt"
	"path/filepath"
	"runtime"
)

func getCaller() string {
	depth := 4
	_, fn, line, ok := runtime.Caller(depth)
	if !ok {
		fn = "???"
		line = 1
	}
	return fmt.Sprintf("%s:%d", filepath.Base(fn), line)
}

func hehe() string {
	s := getCaller()
	return s

}

func wewe() (string, error) {
	m := hehe()
	return m, nil
}

func main() {
	a, _ := wewe()
	fmt.Println(a)
}
