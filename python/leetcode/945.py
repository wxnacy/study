#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:
#  945. 使数组唯一的最小增量  显示英文描述  
#  题目难度 Medium
#  给定整数数组 A，每次 move 操作将会选择任意 A[i]，并将其递增 1。
#  返回使 A 中的每个值都是唯一的最少操作次数。
#  示例 1:
#  输入：[1,2,2]
#  输出：1
#  解释：经过一次 move 操作，数组将变为 [1, 2, 3]。

#  示例 2:
#  输入：[3,2,1,2,1,7]
#  输出：6
#  解释：经过 6 次 move 操作，数组将变为 [3, 4, 1, 2, 5, 7]。
#  可以看出 5 次或 5 次以下的 move 操作是不能让数组的每个值唯一的。
#  提示：

#  0 <= A.length <= 40000
#  0 <= A[i] < 40000

# 第一版效率太低，测试用例超时
#  class Solution(object):
    #  def minIncrementForUnique(self, A):
        #  """
        #  :type A: List[int]
        #  :rtype: int
        #  """
        #  count = 0
        #  tmp = []
        #  dep = []
        #  for i in A:
            #  if i not in tmp:
                #  tmp.append(i)
            #  else:
                #  dep.append(i)
        #  for d in dep:
            #  t = d
            #  while t in tmp:
                #  t+= 1
                #  count += 1
            #  tmp.append(t)
        #  return count

class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # TODO
        if not A:
            return 0
        count = 0
        A.sort()
        be = A[0] + len(A)
        b = list(range(A[0], A[0] + len(A)))
        tmp = []
        for i in A:
            if i not in tmp:
                tmp.append(i)
                #  A.remove(i)
                if i in b:
                    b.remove(i)
        for i in tmp:
            A.remove(i)

        for i in range(len(A)):
            count += b[i] - A[i]
        return count

if __name__ == "__main__":
    s = Solution()
    print(s.minIncrementForUnique([3,2,1,2,1,7]))
    print(s.minIncrementForUnique([0,2,2]))
