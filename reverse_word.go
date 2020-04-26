package main

import (
	"strings"
)

func reverse_words(sent string) {
	words := []string{}
	start, end := 0, 0
	for end < len(sent) {
		if sent[end] == " " {
			words = append(strings.Split(words))
		}
	}
}
