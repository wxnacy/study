package main

import "fmt"

func main() {
	a := map[string]string{"name": "wxnacy"}
	for k, v := range a {
		fmt.Println(k, v)
	}

	b := []int{1, 2, 3}
    fmt.Println("for v := range b")
	for v := range b {
		fmt.Println(v)
	}

    fmt.Println("for i, v := range b")
	for i, v := range b {
		fmt.Println(i, v)
	}

	for range b {
		fmt.Println("Hello World ")
	}

	for i := 0; i < 3; i++ {
		fmt.Println(b[i])
	}

    fmt.Println("for break")
	for i := 0; i < 5; i++ {
		fmt.Println(i)
        if i == 3 {
            break
        }
	}

    fmt.Println("for continue")
	for i := 0; i < 5; i++ {
        if i == 3 {
            continue
        }
		fmt.Println(i)
	}

    fmt.Println("for goto")
    c := 0
    Tag: for c < 5 {
        if c == 3 {
            c++
            goto Tag
        }
		fmt.Println(c)
        c++
	}

	// for true {
	// fmt.Println("Hello World ")
	// }

}
