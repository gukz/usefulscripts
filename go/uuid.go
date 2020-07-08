package main

import (
	"fmt"
	"github.com/google/uuid"
)

func main() {
	taskID := uuid.New().String()
	println(fmt.Sprintf("task_%v", taskID))
}
