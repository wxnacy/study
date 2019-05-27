package main
// 两数之和
// 本题分析文章详见 https://wxnacy.com/leetcode/problems/1-two-sum/

import (
    "testing"
)

// 一遍哈希表
// 执行用时 : 8 ms, 在Two Sum的Go提交中击败了96.37% 的用户
// 内存消耗 : 3.9 MB, 在Two Sum的Go提交中击败了13.80% 的用户
func twoSum(nums []int, target int) []int {
    m := make(map[int]int, 0)
    for i, d := range nums {
        j, ok := m[target - d]
        if ok {
            return []int{j, i}
        }
        m[d] = i
    }
    return []int{0, 0}
}

func TestTwoSum(t *testing.T) {
    rev := twoSum([]int{2, 7, 11, 15}, 9)
    if !ArrayIntEqual(rev, []int{0, 1}) {
        t.Errorf("%v is error", rev)
    }
}
