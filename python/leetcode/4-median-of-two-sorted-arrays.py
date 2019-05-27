#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 寻找两个有序数组的中位数

'''
难度：困难

知识点：数组、二分查找、分治算法

地址： [https://leetcode-cn.com/problems/median-of-two-sorted-arrays/](https://leetcode-cn.com/problems/median-of-two-sorted-arrays/)

```
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

    nums1 = [1, 3]
    nums2 = [2]

    则中位数是 2.0

示例 2:

    nums1 = [1, 2]
    nums2 = [3, 4]

    则中位数是 (2 + 3)/2 = 2.5
```
'''

class Solution:

    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        '''
        执行用时 : 104 ms, 在Median of Two Sorted Arrays的Python3提交中击败了62.78% 的用户
        内存消耗 : 13.4 MB, 在Median of Two Sorted Arrays的Python3提交中击败了47.77% 的用户
        '''
        nums = []

        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            n1 = nums1[i]
            n2 = nums2[j]
            if n1 > n2:
                nums.append(n2)
                j += 1
            else:
                nums.append(n1)
                i += 1

        if i < len(nums1) and j >= len(nums2):
            nums.extend(nums1[i:])
        elif j < len(nums2) and i >= len(nums1):
            nums.extend(nums2[j:])

        k = len(nums)
        if k % 2:
            return nums[k // 2]
        else:
            return (nums[k // 2] + nums[k // 2 - 1]) / 2

    #  def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        #  nums = []
        #  nums.extend(nums1)
        #  nums.extend(nums2)
        #  nums.sort()
        #  nums_len = len(nums)
        #  for i in range(nums_len):
            #  x = i
            #  y = nums_len - i - 1
            #  if x + 1 ==  y:
                #  return float(nums[x] + nums[y]) / 2
            #  if x == y:
                #  return float(nums[x])
        #  return 0

    #  def findMedianSortedArrays1(self, nums1: list, nums2: list) -> float:
        #  l1 = len(nums1)
        #  l2 = len(nums2)
        #  if l1 == 0 and l2 == 0:
            #  return 0

        #  if l1 < l2:
            #  nums1, nums2 = nums2, nums1
        #  l1 = len(nums1)
        #  l2 = len(nums2)

        #  l = l1 + l2

        #  x = 0
        #  y = 0
        #  while x <= l // 2 and y < l2:
            #  if nums1[x] > nums2[y]:
                #  nums1.insert(x, nums2[y])
                #  x += 1
                #  y += 1
            #  else:
                #  if x < l1 - 1:
                    #  x += 1
                #  else:
                    #  nums1.append(nums2[y])
        #  print(nums1)

        #  if l1 % 2:
            #  return float(nums1[l1 // 2])
        #  else:
            #  return float(nums1[l1 // 2] + nums1[l1 // 2 + 1]) / 2



import unittest

class TestMain(unittest.TestCase):

    def setUp(self):
        '''before each test function'''
        pass

    def tearDown(self):
        '''after each test function'''
        pass

    def do(self, func):
        nums1 = [1, 3]
        nums2 = [2]
        self.assertEqual(func(nums1, nums2), 2.0)
        nums1 = [1, 2]
        nums2 = [3, 4]
        self.assertEqual(func(nums1, nums2), 2.5)


    def test_func(self):
        s = Solution()
        self.do(s.findMedianSortedArrays)
        #  self.do(s.findMedianSortedArrays1)

if __name__ == "__main__":
    unittest.main()
