#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 两数之和
#  给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

#  你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

#  示例:

#  给定 nums = [2, 7, 11, 15], target = 9

#  因为 nums[0] + nums[1] = 2 + 7 = 9
#  所以返回 [0, 1]

# 比较简单，但是时间复杂度比较高的暴力遍历
#  class Solution(object):
    #  def twoSum(self, nums, target):
        #  """
        #  :type nums: List[int]
        #  :type target: int
        #  :rtype: List[int]
        #  """
        #  x = -1
        #  y = -1
        #  for i in range(len(nums)):
            #  a = nums[i]
            #  b = target - a
            #  if b in nums[i+1:]:
                #  x = i
                #  for j in range(i+1, len(nums)):
                    #  if nums[j] == b:
                        #  y = j
                        #  break
                #  break
        #  return [x, y]

class Solution(object):
    '''使用字典，可以进行一次遍历就得出结果'''
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        x = -1
        y = -1
        m = {}
        for i in range(len(nums)):
            a = nums[i]
            b = target - a
            if b in m:
                x = i
                y = m[b]
                return [y, x]
            m[a] = i
        return [x, y]

if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9) == [0, 1])
    print(s.twoSum([2,5,5,11], 10) == [1, 2])
    print(s.twoSum([0,4,3,0], 0) == [0, 3])
    print(s.twoSum([-3,4,3,90], 0) == [0, 2])
    print(s.twoSum([3,2,4], 6) == [1, 2])
    print(s.twoSum([3,2,4], 6) == [1, 2])
    print(s.twoSum([-1,-2,-3,-4,-5], -8) == [2, 4])

