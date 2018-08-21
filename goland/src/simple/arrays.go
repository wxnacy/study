package main

import "fmt"

func main() {
    var a [2] int   // null
    // var a = []map[string]string{}    // []
    fmt.Println(a)
    a[0] = 12
    fmt.Println(a)

    a = [2]int{3, 4}
    fmt.Println(a)

    b := [...]int{2, 3, 4}
    fmt.Println(b)

    var c [2][3] int 
    c[0][0] = 1
    fmt.Println(c)

    d := [2][2]int{{1, 2}, {3, 4}}
    fmt.Println(d)

    e := []int{1, 2, 3}
    fmt.Println(e)

    Test(e)

    var f = []int{1, 2}
    fmt.Println(f)
    f = append(f, 3, 4)
    fmt.Println(f)
}

func Test(a []int) {
    fmt.Println(a)
}
