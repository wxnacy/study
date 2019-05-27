package main
// 整数反转
// 本题分析文章详见 https://wxnacy.com/leetcode/problems/7-reverse-integer/

import (
    "testing"
    "math"
)

// 执行用时 : 0 ms, 在Reverse Integer的Go提交中击败了100.00% 的用户
// 内存消耗 : 2.2 MB, 在Reverse Integer的Go提交中击败了33.94% 的用户
func reverse(x int) int {
    rev := 0
    for x != 0 {
        pop := x % 10
        rev = rev * 10 + pop
        x /= 10
        if rev > math.MaxInt32 || ( rev == ( math.MaxInt32 - 7 ) / 10 && pop > 7  ) {
            return 0
        }
        if rev < math.MinInt32 || ( rev == ( math.MinInt32 + 8 ) / 10 && pop < -8 ) {
            return 0
        }
    }
    return rev
}

func TestReverse(t *testing.T) {
    sources := map[int]int{
        123: 321,
        -123: -321,
        120: 21,
        -12300: -321,
        1534236469: 0,
        -1563847412: 0,
        0: 0,
    }
    for i, d := range sources {
        rev := reverse(i)
        if rev != d {
            t.Errorf("%d is error", rev)
        }

    }

}
