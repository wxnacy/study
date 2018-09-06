package main

import "fmt"

func main() {
    var i []int     // []
    fmt.Println(i)
    i = append(i, 1, 2)
    fmt.Println(i)

    i = i[:]
    i = []int{1, 2, 3,4}
    fmt.Println(i)
    i = []int{1, 2, 3, 4, 5}
    fmt.Println(i)

    i = Remove(i, 0)
    fmt.Println(i)


    fmt.Println("make")
    var m = make([]int, 3, 4)
    fmt.Printf("slice %v len %d cap %d", m, len(m), cap(m))
    for i := range []int{1, 2, 3} {
        m[i] = 4
    }
    fmt.Println(m)

    m = []int{1, 2, 3, 4, 5}
    fmt.Println(m)

	var a [2]int // null
	// var a = []map[string]string{}    // []
	fmt.Println(a)
	a[0] = 12
	fmt.Println(a)

    // fmt.Println(append(a, i[:]...))

	a = [2]int{3, 4}
	fmt.Println(a)

    // 一旦确定长度，便不能通过初始化的方式更改长度
    // a = [4]int{5, 6, 7, 8}
    // fmt.Println(a)

	b := [...]int{2, 3, 4}
	fmt.Println(b)


	var c [2][3]int
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

    h := []int{1, 2, 3, 4, 5, 6, 7}
    fmt.Println(h[:])
    fmt.Println(h[0:])
    fmt.Println(h[0:len(h)])
    fmt.Println(h[2:4])
    fmt.Println(h[:4])
    fmt.Println(h[:4])


    var n = []int{1, 2}
    var l = make([]int, len(n), cap(n) * 2)
    copy(l, n)
    fmt.Println(l)

}

func Test(a []int) {
	fmt.Println(a)
}

func Remove(slice []int, s int) []int {
    return append(slice[:s], slice[s+1:]...)
}
