#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 回文数

# 使用字符比较首尾 平均 124 ms
#  class Solution(object):
    #  def isPalindrome(self, x):
        #  """
        #  :type x: int
        #  :rtype: bool
        #  """
        #  if x == 0:
            #  return True
        #  if x < 0:
            #  return False
        #  if x % 10 == 0:
            #  return False
        #  a = str(x)
        #  for i in range(len(a)):
            #  j = len(a) -1 - i
            #  if i <= j and a[i] != a[j]:
                #  return False
        #  return True

class Solution(object):
    def isPalindrome(self, x):
        """
        依然是数学的方式 平均 116 ms
        :type x: int
        :rtype: bool
        """
        if x == 0:
            return True
        if x < 0:
            return False
        if x % 10 == 0:
            return False
        temp = 0
        while x > temp:
            pre = x % 10
            x  = (x - pre) // 10
            temp = temp * 10 + pre
        return x == temp or x == temp // 10
        if x == temp:
            return True
        else:
            return False

        

if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(121))
    print(s.isPalindrome(0))
    print(s.isPalindrome(11))
