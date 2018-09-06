package main

import (
    "fmt"
    "sync"
)

func main() {
    var wg sync.WaitGroup
    wg.Add(2)
    go func() {
        fmt.Println(1)
        wg.Done()
    }()
    go func() {
        fmt.Println(2)
        wg.Done()
    }()
    fmt.Println(3)
    wg.Wait()
}
