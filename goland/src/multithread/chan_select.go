package main

import (
    "fmt"
    "time"
)

func main() {
    count := 0
    var c = make(chan int, 1)
    for i := 0; i < 10; i++ {
        go func() {
            time.Sleep(1 * time.Second)
            count++
            if count == 10 {
                c <- 1
            }
        }()
    }

    t := time.NewTicker(200 * time.Millisecond)
    defer t.Stop()

    Loop:
    for true{
        select {
            case <-t.C: {
                fmt.Println("inprogress")
            }
            case <- c: {
                fmt.Println("Done")
                break Loop
            }
        }
    }

}
