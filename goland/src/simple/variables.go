package main

import "fmt"

var (
    id int
    name string
)

func main(){
    var a = 1
    var b string = "b"
    c := 10
    fmt.Println(a, b, c)
    d := c
    c = 20
    fmt.Println(d)

    e, f, g := 1, 2, 3
    fmt.Println(e, f, g)

    id = 1
    name = "wxnacy"
    fmt.Println(id, name)

    var h *int = &c
    fmt.Println(*h)
    c = 30
    fmt.Println(*h)

    fmt.Println('s')
}
