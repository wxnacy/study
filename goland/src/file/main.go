package main

import (
    "fmt"
    "os"
    "log"
)

func main() {
    fmt.Println("Hello World") 
    f, _ := os.OpenFile("message")
    b := make([]byte, 0)

    if _, err := io.ReadFull(f, b); err != nil {
		log.Fatal(err)
	}
    fmt.Println(b)
}
