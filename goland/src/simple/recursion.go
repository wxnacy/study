package main

import "fmt"

func main() {
    for i := 1; i < 10; i++ {
        fmt.Println(f1(i))
    }
}

func f1(n int) int {
    if n < 2 {
        return n
    }
    return f1( n - 1 ) + f1( n - 2 )
}
