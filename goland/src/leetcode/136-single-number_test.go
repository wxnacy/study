package main
// 只出现一次的数字
// 本题分析文章详见 https://wxnacy.com/leetcode/problems/136-single-number/

import (
    "testing"
)

// 异或运算
// 执行用时 : 12 ms, 在Single Number的Go提交中击败了99.25% 的用户
// 内存消耗 : 4.9 MB, 在Single Number的Go提交中击败了55.43% 的用户
func singleNumber(nums []int) int {
    for i := 1; i < len(nums); i++ {
        nums[0] = nums[0] ^ nums[i]
    }
    return nums[0]
}

func TestSingleNumber(t *testing.T) {
    sources := map[int][]int{
        4: []int{4, 1, 2, 1, 2},
        1: []int{2, 2, 1},
    }
    for i, d := range sources {
        rev := singleNumber(d)
        if rev != i {
            t.Errorf("%d is error", rev)
        }

    }

}
