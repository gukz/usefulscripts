package main

import (
	"os"
	"text/template"
)

var i = `
{{- /* 这里是 另外一个注释  */ -}}
 这里是 注释  
{{.Count}} items are made of {{.Material}}
{{if .Count}} 这里是 pipline
hehe
{{else}}
没有count
{{end}}

{{range $index, $element := .Arr}} {{$index}} what {{$element}} {{end}}
`

type Invertory struct {
	Count    uint
	Material string
	Arr      []string
}

func main() {
	iobj := Invertory{Count: 2, Material: "hello", Arr: []string{"1aa", "2bbbb", "3ccccc"}}
	tmpl, err := template.New("test").Parse(i)
	if err != nil {
		panic(err)
	}
	err = tmpl.Execute(os.Stdout, iobj)
	if err != nil {
		panic(err)
	}
}
