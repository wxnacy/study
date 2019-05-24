#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 合并两个有序数组 简单

'''
https://leetcode-cn.com/problems/merge-sorted-array/

给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]
'''

class Solution:
    def merge(self, nums1: 'List[int]', m: int, nums2: 'List[int]', n: int) -> None:
        """
        先合并，在使用快速排序
        执行用时 : 60 ms, 在Merge Sorted Array的Python3提交中击败了49.81% 的用户
        内存消耗 : 12.9 MB, 在Merge Sorted Array的Python3提交中击败了99.08% 的用户
        """
        if not nums1 or not nums2:
            return

        for i in range(len(nums2)):
            nums1[m + i] = nums2[i]

        def _sort_once(nums, left, right):
            x = left
            y = right
            pivot = nums[left]
            while x < y:
                while x < y and nums[y] >= pivot:
                    y -= 1
                nums[x] = nums[y]
                while x < y and nums[x] <= pivot:
                    x += 1
                nums[y] = nums[x]

            nums[x] = pivot

            return x

        def _sort(nums, left, right):
            if left < right:
                pivot_index = _sort_once(nums, left, right)

                _sort(nums, left, pivot_index - 1)
                _sort(nums, pivot_index + 1, right)


        _sort(nums1, 0, len(nums1) - 1)

    def merge1(self, nums1: 'List[int]', m: int, nums2: 'List[int]', n: int) -> None:
        """
        先合并，在使用 sort 排序
        """
        if not nums1 or not nums2:
            return
        for i in range(len(nums2)):
            nums1[m + i] = nums2[i]
        nums1.sort()

    def merge2(self, nums1: 'List[int]', m: int, nums2: 'List[int]', n: int) -> None:
        """
        直接从最后开始按照大数开始插入
        """
        if not nums1 or not nums2:
            return
        #  i = m + n -1
        x = m - 1
        y = n - 1
        l = len(nums1)
        for j in range(l):
            i = l - j - 1
            if y < 0 and x < 0:
                return
            if y >=0 and x >= 0:
                if nums1[x] > nums2[y]:
                    nums1[i] = nums1[x]
                    x -= 1
                else:
                    nums1[i] = nums2[y]
                    y -= 1
            elif y >= 0 and x < 0:
                nums1[i] = nums2[y]
                y -= 1
            elif y < 0 and x >= 0:
                nums1[i] = nums1[x]
                x -= 1
            #  i -= 1



s = Solution()

import unittest
import utils

class TestMain(unittest.TestCase):

    def setUp(self):
        '''before each test function'''
        pass

    def tearDown(self):
        '''after each test function'''
        pass

    def do(self, func):
        nums1 = [1,2,3,0,0,0]
        nums2 = [2,5,6]
        func(nums1, 3, nums2, 3)
        self.assertEqual(nums1, [1,2,2,3,5,6])
        nums1 = []
        nums2 = []
        func(nums1, 0, nums2, 0)
        self.assertEqual(nums1, [])
        nums1 = [1, 2]
        nums2 = []
        func(nums1, 2, nums2, 0)
        self.assertEqual(nums1, [1, 2])
        nums1 = [2, 0]
        nums2 = [1]
        func(nums1, 1, nums2, 1)
        self.assertEqual(nums1, [1, 2])
        nums1 = [1,2,4,5,6,0]
        nums2 = [3]
        func(nums1, 5, nums2, 1)
        self.assertEqual(nums1, [1, 2, 3, 4, 5, 6])
        nums1 = [2,4,6,0,0,0]
        nums2 = [1, 3, 5]
        func(nums1, 3, nums2, 3)
        self.assertEqual(nums1, [1, 2, 3, 4, 5, 6])

    def test_func(self):
        self.do(s.merge)
        self.do(s.merge1)
        self.do(s.merge2)

if __name__ == "__main__":
    count = 1000
    nums1 = [2,4,6,0,0,0]
    nums2 = [1, 3, 5]
    utils.print_func_run_time(count, s.merge, nums1=nums1, m = 3, nums2 = nums2, n = 3)
    utils.print_func_run_time(count, s.merge1, nums1=nums1, m = 3, nums2 = nums2, n = 3)
    utils.print_func_run_time(count, s.merge2, nums1=nums1, m = 3, nums2 = nums2, n = 3)
    unittest.main()
