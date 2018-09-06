package main

import (
    "fmt"
)

func Func1(call func(a int, b int) int) {
    fmt.Println(call(1, 2))
}

type Callback func(a int) int

func Func2(b int, callback Callback) int {
    return callback(b)
}

func Func3(a int, call func(b int) int) int {
    return call(a)
}

func main() {
    Func1(func(a int, b int) int {
        return a + b
    })

    res := Func2(1, func(a int) int{
        return a + 2
    })
    fmt.Println(res)

    res = Func3(1, func(b int) int {
        return b
    })
    fmt.Println(res)

}
