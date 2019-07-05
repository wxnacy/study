package main

import (
    "testing"
    "fmt"
)

var LIST = []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}
// var LIST []int

// func GetList() {
    // if LIST == [] {
        // LIST = make([]int, 0)
        // for i := 0; i < 10000; i++ {
            // LIST = append(LIST, i)
        // }
    // }
    // return LIST
// }

func For() {
    var total int
    for i := 0; i < len(LIST); i++ {
        for k := 0; k < len(LIST); k++ {
            total += LIST[k]
        }
    }
}

func While() {
    var total int
    i := 0
    for i < len(LIST) {
        total += LIST[i]
        i++
    }
}

func ForEach(b *testing.B) {
    var total int
    for _, d := range LIST {
        total += d
    }
}

func BenchmarkWhile(b *testing.B) {
    var total int
    i := 0
    for i < len(LIST) {
        total += LIST[i]
        i++
    }
}

func BenchmarkForEach(b *testing.B) {
    var total int
    for _, d := range LIST {
        total += d
    }
}

func BenchmarkFor(b *testing.B) {
    For()

}

func main() {

    fmt.Print(LIST)
}
