package main

import "fmt"

func main() {
    a := map[string]string{"name": "wxnacy"}
    for k, v := range a {
        fmt.Println(k, v)
    }

    b := []int{1, 2, 3}
    for v := range b {
        fmt.Println(v)
    }

    for i, v := range b {
        fmt.Println(i, v)
    }

    for range b {
        fmt.Println("Hello World ")
    }

    for i := 0; i < 3; i++ {
        fmt.Println(b[i])
    }

    // for true {
        // fmt.Println("Hello World ")
    // }

}
