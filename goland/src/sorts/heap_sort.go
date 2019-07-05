package main

import (
    "fmt"
)

func HeapSort(nums []int) {
    num_len := len(nums)
    i := (num_len >> 1) - 1
    for i > -1 {
        heapify(nums, i, num_len)
        i--
    }

    for i := num_len - 1; i > -1; i-- {
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, 0, i)
    }
    fmt.Println(nums)
}

func heapify(nums []int, i, num_len int) {
    k := i
    left, right := i * 2 + 1, i * 2 + 2
    if left < num_len && nums[left] > nums[k]{
        k = left
    }
    if right < num_len && nums[right] > nums[k] {
        k = right
    }
    if k != i {
        nums[k], nums[i] = nums[i], nums[k]
        heapify(nums, k, num_len)
    }
}

func main() {
    var nums = []int{6, 5, 8,4, 7, 2, 9, 3, 1}
    HeapSort(nums)
    
}
