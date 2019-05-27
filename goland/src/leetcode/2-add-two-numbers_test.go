package main
// 两数相加
// 本题分析文章详见 https://wxnacy.com/leetcode/problems/2-add-two-numbers/

import (
    "testing"
)

// 初等数学
// 执行用时 : 16 ms, 在Add Two Numbers的Go提交中击败了94.74% 的用户
// 内存消耗 : 5.1 MB, 在Add Two Numbers的Go提交中击败了42.98% 的用户
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    l3 := &ListNode{Val: 0}
    l4 := l3
    carry := 0
    for l1 != nil || l2 != nil || carry > 0 {
        n := carry
        if l1 != nil {
            n += l1.Val
            l1 = l1.Next
        }
        if l2 != nil {
            n += l2.Val
            l2 = l2.Next
        }
        l4.Next = &ListNode{Val: n % 10}
        carry = n / 10
        l4 = l4.Next
    }
    return l3.Next
}


func TestAddTwoNumbers(t *testing.T) {
    sources := [][][]int{
        [][]int{[]int{2, 4, 3}, []int{5, 6, 4}, []int{7, 0, 8}},
        [][]int{[]int{0}, []int{0}, []int{0}},
        [][]int{[]int{1, 8}, []int{0}, []int{1, 8}},
        [][]int{[]int{5}, []int{5}, []int{0, 1}},
    }
    for _, d := range sources {
        // t.Error(d[2])
        rev := addTwoNumbers(Array2ListNode(d[0]), Array2ListNode(d[1]))
        if !ArrayIntEqual(ListNode2Array(rev), d[2]) {
            t.Errorf("%v is error", ListNode2Array(rev))
        }

    }

}
