package main

import "fmt"

const (
    Female = 1
    Male = 2
)

const (
    e = iota
    f = iota
    g
    h = "h"
    i
    j = 5
    k
    l = iota
    m
    n = 100
    o
    p = 1 << iota
    r = 1 << iota
)

func main(){
    const a = 1
    const b string = "b"

    const c, d = 2, 3

    fmt.Println(a, b, c, d)
    fmt.Println(Female, Male)
    fmt.Println(e, f, g, h, i, j, k, l, m, n, o, p, r)
}
