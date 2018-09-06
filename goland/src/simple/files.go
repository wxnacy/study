package main

import (
	"fmt"
	"log"
	"os"
)

func main() {
	Func1()
}

func Func1() {
	fmt.Println("Hello World ")
	file, err := os.Stat("loops.go")
	if err != nil {
		// fmt.Println(err)
		log.Fatal(err)
	}

	fmt.Println(file.Name(), file.Size(), file.Mode(), file.ModTime(),
		file.IsDir(), file.Sys())
	fmt.Printf("System interface type: %T\n", file.Sys())
	fmt.Printf("System info: %+v\n\n", file.Sys())
}
