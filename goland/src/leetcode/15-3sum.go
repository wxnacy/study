package main
// 三数之和

import (
    "testing"
    "sort"
)
// 执行用时 : 1356 ms, 在3Sum的Go提交中击败了85.58% 的用户
// 内存消耗 : 155.8 MB, 在3Sum的Go提交中击败了12.01% 的用户
func threeSum(nums []int) [][]int {
    res := make([][]int, 0)
    sort.Ints(nums)
    i := 0
    length := len(nums)
    for i < length - 2 {
        if nums[i] > 0 {
            break
        }
        left := i + 1
        right := length - 1
        for left < right {
            s := nums[i] + nums[left] + nums[right]
            if s == 0 {
                res = append(res, []int{nums[i], nums[left], nums[right]})
            }
            if s <= 0 {
                left++
                for left < right && nums[left] == nums[left - 1] {
                    left++
                }
            } else {
                right--
                for left < right && nums[right] == nums[right + 1] {
                    right--
                }
            }
        }
        i++
        for nums[i] == nums[i-1] {
            i++
        }
    }
    return res
}

func TestThreeSum(t *testing.T) {

    rev := threeSum([]int{-1, 0, 1, 2, -1, -4})
    if rev != [][]int{[]int{-1, -1, 2}, []int{-1, 0, 1}} {
        t.Errorf("%d is error", rev)
    }

}
