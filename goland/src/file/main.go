package main

import (
    "fmt"
    "os"
    "log"
    "io"
)

func main() {
    f, err := os.Open("message")
    if err != nil {
		log.Fatal(err)
	}
    b := make([]byte, 8)

    if _, err := io.ReadFull(f, b); err != nil {
		log.Fatal(err)
	}
    fmt.Printf("%s\n", b)
}
