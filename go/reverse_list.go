package main

import (
	"fmt"
)

type Node struct {
	v    int
	next *Node
}

func reverseList(root *Node) *Node {
	p := root
	head := &Node{v: 0, next: nil}
	for p != nil {
		p_next := p.next
		p.next = head.next
		head.next = p
		p = p_next
	}
	return head.next
}

func main() {
	list1 := &Node{v: 1, next: &Node{v: 2, next: &Node{v: 3, next: nil}}}
	list2 := reverseList(list1)
	fmt.Printf("%+v", list2)
}
