package main

import (
    "fmt"
)

func QuickSort(nums []int) {
    quickSort(nums, 0, len(nums) - 1)
}

func quickSort(nums []int, left, right int) {
    if right >= left {
        return
    }
    pivot := partition(nums, left, right)
    quickSort(nums, left, pivot - 1)
    quickSort(nums, pivot + 1, right)

}

func partition(nums []int, left, right int) int {
    t := nums[left]
    x := left
    y := right
    for x < y {
        for x < y && nums[y] >= t {
            y--
        }
        nums[x] = nums[y]
        for x < y && nums[x] <= t {
            x++
        }
        nums[y] = nums[x]
    }
    nums[x] = t
    return x
}

func main() {
    var nums = []int{6, 5, 8,4, 7, 2, 9, 3, 1}
    QuickSort(nums)
    fmt.Println(nums)
    
}
