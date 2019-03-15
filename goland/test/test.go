package main

import (
    "fmt"; "os"
)

func test() {;a := "Hello World ";fmt.Println(a)}

func main() {
    fmt.Println(os.Getwd())
    test()
}
