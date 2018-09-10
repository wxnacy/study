package main

import (
    "fmt"
    // "time"
)

func PrintNum(a int) {
    fmt.Println(a)
}

func main() {
    go PrintNum(1)
    go PrintNum(2)

    // time.Sleep(1 * time.Second)
    fmt.Println("Done")
}
