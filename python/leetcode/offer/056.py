#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

'''
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

 

示例 1：

输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]
示例 2：

输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]
 

限制：

2 <= nums <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

import unittest

class Solution:
    def singleNumbers(self, nums):
        #  a, res = 0, [0, 0]
        #  for num in nums:
            #  a ^= num
        #  print(a)
        xor, ans = 0, [0, 0]
        for num in nums:
            xor ^= num
        print(xor)
        low = xor ^ (xor - 1) & xor
        print(low)
        for num in nums:
            tar = not num & low
            print(tar)
            ans[tar] ^= num
        return ans


s = Solution()


class TestMain(unittest.TestCase):

    def setUp(self):
        '''before each test function'''
        pass

    def tearDown(self):
        '''after each test function'''
        pass

    def do(self, func):
        '''todo'''
        r1 = func([4, 1, 4, 6])
        self.assertEqual(r1, [1, 6])
        #  r1 = func([1,2,10,4,1,4,3,3])
        #  self.assertEqual(r1, [10, 2])

    def test_func(self):
        self.do(s.singleNumbers)

if __name__ == "__main__":
    unittest.main()
