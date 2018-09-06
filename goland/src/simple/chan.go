package main

import (
    "fmt"
    "time"
)

func Produce(p chan<- int) {
    for i := 0; i < 10; i++ {
        p <- i
    }
}

func Consumer(p <-chan int) {
    for i := 0; i < 10; i++ {
        v := <- p
        fmt.Println(v)
    }
}

func main() {
    go fmt.Println(1)
    go func (a int) {
        fmt.Println(a)
    }(3)
    fmt.Println(2)
    time.Sleep(1 * time.Second)

    var c chan int
    fmt.Println(c)
    go func () {
        c1 := <- c
        fmt.Println(c1)
    }()
    var c2 = make(chan<- int, 1)
    c2 <- c
    fmt.Println(c2)
    time.Sleep(1 * time.Second)

    // ch :=make(chan int,1)
    // ch <- 1
    // go func() {
        // v := <-ch
        // fmt.Println(v)
    // }()
    // time.Sleep(1 * time.Second)
    // fmt.Println("2")

    // ch = make(chan int, 10)
    // go Produce(ch)
    // go Consumer(ch)

    // time.Sleep(1 * time.Second)

}
