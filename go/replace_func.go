package main

import (
	"fmt"
	"reflect"
	"syscall"
	"unsafe"
)

// 动态替换函数体
// 参考 https://berryjam.github.io/2018/12/golang%E6%9B%BF%E6%8D%A2%E8%BF%90%E8%A1%8C%E6%97%B6%E5%87%BD%E6%95%B0%E4%BD%93%E5%8F%8A%E5%85%B6%E5%8E%9F%E7%90%86/

func JumpAssemblyDataWithReflect(p uintptr) []byte {
	return []byte{
		0x48, 0xC7, 0xC2,
		byte(p),
		byte(p >> 8),
		byte(p >> 16),
		byte(p >> 24), // mov rdx,p
		0xFF, 0xe2,    // jmp rdx而不是jmp [rdx]
	}
}

func getPageWithReflect(p uintptr) []byte {
	return (*(*[0xFFFFFF]byte)(unsafe.Pointer(p & ^uintptr(syscall.Getpagesize()-1))))[:syscall.Getpagesize()]
}

func RawMemoryAccessWithReflect(p uintptr) []byte {
	return (*(*[0xFF]byte)(unsafe.Pointer(p)))[:]
}

func replaceWithReflect(from, to interface{}) {

	jumpAndExecToAssemblyData := JumpAssemblyDataWithReflect(reflect.ValueOf(to).Pointer())
	funcLocation := reflect.ValueOf(from).Pointer()
	window := RawMemoryAccessWithReflect(funcLocation)

	page := getPageWithReflect(funcLocation)
	syscall.Mprotect(page, syscall.PROT_READ|syscall.PROT_WRITE|syscall.PROT_EXEC)

	copy(window, jumpAndExecToAssemblyData)
}

func main() {
	replaceWithReflect(e, f)
	fmt.Println(e(1, 5))
	replaceWithReflect(g, h)
	fmt.Println(g())
}

func e(a, b int) float64 {
	fmt.Println(a + b)
	fmt.Println("func e")
	return 0
}

func f(a, b int) float64 {
	fmt.Println(a - b)
	fmt.Println("func f")
	return 3.14
}

func g() string {
	return "return by g()"
}

func h() string {
	return "return by h()"
}
