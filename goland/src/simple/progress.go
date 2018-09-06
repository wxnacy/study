package main

import (
    "fmt"
    "time"
)

func main() {
    fmt.Println("Hello World")
    var d = make(chan int, 1)
    begin := time.Now().Unix()
    fmt.Println(begin)

    t := time.NewTicker(200 * time.Millisecond)
	defer t.Stop()

    go func (){
        for i := 0; i < 10; i++ {
            fmt.Println(i)
            time.Sleep(1 * time.Second)
            if i == 9 {
                d <- 1
            }
        }
    }()
    fmt.Println(t.C)

    Loop:
    for true{
        select {
            case <-t.C: {
                fmt.Println("in progress")
            }
            case <- d: {
                fmt.Println("Done")
                break Loop
            }
        }
    }
}
