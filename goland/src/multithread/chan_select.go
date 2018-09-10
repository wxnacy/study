package main

import (
    "fmt"
    "time"
)

func PrintNum(a int) {
    fmt.Println(a)
}

func main() {
    var c = make(chan int, 1)
    for i := 0; i < 5; i++ {
        time.Sleep(200 * time.Millisecond)
        go func() {
            PrintNum(i)
            if i == 4 {
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
