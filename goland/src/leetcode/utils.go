package main

import (
    "fmt"
)

func StringSliceEqualBCE(a, b []string) bool {
    if len(a) != len(b) {
        return false
    }

    if (a == nil) != (b == nil) {
        return false
    }

    b = b[:len(a)]
    for i, v := range a {
        if v != b[i] {
            return false
        }
    }

    return true
}

func ArrayIntEqual(a, b []int) bool {
    if len(a) != len(b) {
        return false
    }

    if (a == nil) != (b == nil) {
        return false
    }

    b = b[:len(a)]
    for i, v := range a {
        if v != b[i] {
            return false
        }
    }

    return true
}

type ListNode struct {
    Val int
    Next *ListNode
}

func Array2ListNode(arr []int) *ListNode {
    l := &ListNode{Val: 0}
    l2 := l
    for _, d := range arr {
        l2.Next = &ListNode{Val: d}
        l2 = l2.Next
    }
    return l.Next
}

func ListNode2Array(l *ListNode) []int {
    arr := make([]int, 0)
    for l != nil {
        arr = append(arr, l.Val)
        l = l.Next
    }
    return arr
}

func main() {
    ln := Array2ListNode([]int{1, 2})
    arr := ListNode2Array(ln)
    fmt.Println(ln)
    fmt.Println(arr)
}
