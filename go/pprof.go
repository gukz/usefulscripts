package main

import (
	"fmt"
	"os"
	"runtime/pprof"
)

func init() {
	cpuProfile, _ := os.Create("cpu_profile")
	pprof.StartCPUProfile(cpuProfile)
	defer pprof.StopCPUProfile()
}

func main() {
	fmt.Println("test")
}
