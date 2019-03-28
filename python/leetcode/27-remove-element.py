#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 移除元素
# 难度 简单

'''
给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

示例 1:

给定 nums = [3,2,2,3], val = 3,

函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,1,2,2,3,0,4,2], val = 2,

函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。

注意这五个元素可为任意顺序。

你不需要考虑数组中超出新长度后面的元素。
说明:

为什么返回数值是整数，但输出的答案是数组呢?

请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

// nums 是以“引用”方式传递的。也就是说，不对实参作任何拷贝
int len = removeElement(nums, val);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
'''

def removeElement(nums, val) -> int:
    if not nums:
        return 0
    i = 0
    for j in range(len(nums)):
        if nums[j] == val:
            if nums[i] != val:
                i = j
        else:
            if nums[i] != val:
                i += 1
            else:
                if nums[i] == val:
                    temp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = temp
                    i += 1
    return i

def removeElement1(nums, val) -> int:
    i = 0
    for n in nums:
        if n != val:
            nums[i] = n
            i+=1
    return i

def removeElement2(nums, val) -> int:
    i = 0
    n = len(nums)
    while i < n:
        if nums[i] == val:
            nums[i] = nums[n - 1]
            n -= 1
        else:
            i += 1
    return i

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
        n = [3,2,2,3]
        self.assertEqual(func(n, 3), 2)
        #  self.assertEqual(n[0:2], [2, 2])
        n = [0,1,2,2,3,0,4,2]
        self.assertEqual(func(n, 2), 5)
        #  self.assertEqual(n[0:5], [0, 1, 3, 0, 4])
        n = [2]
        self.assertEqual(func(n, 3), 1)
        #  self.assertEqual(n[0:1], [2])
        n = [3, 3]
        self.assertEqual(func(n, 5), 2)
        #  self.assertEqual(n[0:2], [3, 3])

    def test_func(self):
        self.do(removeElement)
        self.do(removeElement1)
        self.do(removeElement2)

if __name__ == "__main__":
    count = 10000
    nums = [0,1,2,2,3,0,4,2]
    utils.print_func_run_time(count, removeElement, nums = nums, val = 2)
    utils.print_func_run_time(count, removeElement1, nums = nums, val = 2)
    utils.print_func_run_time(count, removeElement2, nums = nums, val = 2)
    unittest.main()
