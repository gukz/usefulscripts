package main

import (
	"fmt"
	"os"
	"runtime"
	"runtime/pprof"
)

var (
	cpuProfile     = "cpu_profile"
	memProfile     = "mem_profile"
	memProfileRate = 10
)

func startCPUProfile() {
	f, err := os.Create(cpuProfile)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Can not create cpu profile output file: %s", err)
		return
	}
	if err := pprof.StartCPUProfile(f); err != nil {
		fmt.Fprintf(os.Stderr, "Can not start cpu profile: %s", err)
		f.Close()
		return
	}
}

func stopCPUProfile() {
	pprof.StopCPUProfile()
}

func startMemProfile() {
	runtime.MemProfileRate = memProfileRate
}

func stopMemProfile() {
	f, err := os.Create(memProfile)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Can not create mem profile output files: %s", err)
		return
	}
	if err = pprof.WriteHeapProfile(f); err != nil {
		fmt.Fprintf(os.Stderr, "Can not write %s: %s", memProfile, err)
	}
	f.Close()
}

func main() {
	fmt.Println("test")
}
