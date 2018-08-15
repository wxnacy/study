package main

import "fmt"

func main(){

    a := []int{1, 2, 3, 4, 5, 6}

    fmt.Println(a[:])
    fmt.Println(a[:3])
    fmt.Println(a[1:3])
    fmt.Println(a[1:])


    var b = make([]int, 3, 5)
    fmt.Println(len(b), cap(b), b)
    b = append(b, 1, 2, 3)
    fmt.Println(b)

    fmt.Println(a)

    var c = make([]int, 6, 7)
    copy(c, a)
    fmt.Println(c)

    fmt.Println(len(a), cap(a))
}
