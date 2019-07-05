#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

def quick_sort(nums):

    def partition(nums, left, right):
        tmp = nums[left]
        x = left
        y = right
        while x < y:
            while x < y and nums[y] >= tmp:
                y -= 1
            nums[x] = nums[y]
            while x < y and nums[x] <= tmp:
                x += 1
            nums[y] = nums[x]
        nums[x] = tmp
        return x

    def _sort(nums, left, right):
        if left >= right:
            return

        part = partition(nums, left, right)
        _sort(nums, left, part - 1)
        _sort(nums, part + 1, right)

    _sort(nums, 0, len(nums) - 1)


if __name__ == "__main__":
    nums = [6, 7, 4, 5, 9, 1, 3, 2, 8]
    quick_sort(nums)
    print(nums)

