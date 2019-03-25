#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 罗马数字转整数

#  罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

#  字符          数值
#  I             1
#  V             5
#  X             10
#  L             50
#  C             100
#  D             500
#  M             1000
#  例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

#  通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

#  I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
#  X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
#  C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
#  给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

#  示例 1:

#  输入: "III"
#  输出: 3
#  示例 2:

#  输入: "IV"
#  输出: 4
#  示例 3:

#  输入: "IX"
#  输出: 9
#  示例 4:

#  输入: "LVIII"
#  输出: 58
#  解释: L = 50, V= 5, III = 3.
#  示例 5:

#  输入: "MCMXCIV"
#  输出: 1994
#  解释: M = 1000, CM = 900, XC = 90, IV = 4.

ROMAN_TO_INT1 = {
    "I":             1,
    "V":             5,
    "X":             10,
    "L":             50,
    "C":             100,
    "D":             500,
    "M":             1000,
}

ROMAN_TO_INT2 = {
    "IV":            4,
    "IX":            9,
    "XL":            40,
    "XC":            90,
    "CD":            400,
    "CM":            900,
}

# 使用字符串替换 平均 184 ms  太慢

#  class Solution(object):
    #  def romanToInt(self, s):
        #  """
        #  :type s: str
        #  :rtype: int
        #  """
        #  for k, v in ROMAN_TO_INT2.items():
            #  s = s.replace(k, '-{}'.format(v))
        #  for k, v in ROMAN_TO_INT1.items():
            #  s = s.replace(k, '-{}'.format(v))
        #  nums = s.split("-")
        #  return sum([int(o) for o in nums if o])

#  使用一次循环，碰见了组合先组合取值，再看单个的，最后相加，评论 140 ms 快乐一些
#  class Solution(object):
    #  def romanToInt(self, s):
        #  """
        #  :type s: str
        #  :rtype: int
        #  """
        #  nums = []
        #  i = 0
        #  while i < len(s):
            #  if i == len(s) - 1:
                #  nums.append(ROMAN_TO_INT1[s[i]])
                #  break
            #  if s[i] == "I" and s[i+1] == "V":
                #  nums.append(4)
                #  i += 1
            #  elif s[i] == "I" and s[i+1] == "X":
                #  nums.append(9)
                #  i += 1
            #  elif s[i] == "X" and s[i+1] == "L":
                #  nums.append(40)
                #  i += 1
            #  elif s[i] == "X" and s[i+1] == "C":
                #  nums.append(90)
                #  i += 1
            #  elif s[i] == "C" and s[i+1] == "D":
                #  nums.append(400)
                #  i += 1
            #  elif s[i] == "C" and s[i+1] == "M":
                #  nums.append(900)
                #  i += 1
            #  else:
                #  nums.append(ROMAN_TO_INT1[s[i]])
            #  i+=1
        #  return sum(nums)

# 对上面的方法进行了优化 平均 100 ms 有快乐一些
#  class Solution(object):
    #  def romanToInt(self, s):
        #  """
        #  :type s: str
        #  :rtype: int
        #  """
        #  nums = []
        #  i = 0
        #  kk = [k for k, v in ROMAN_TO_INT2.items()]
        #  while i < len(s):
            #  if i == len(s) - 1:
                #  nums.append(ROMAN_TO_INT1[s[i]])
                #  break
            #  ss = s[i] + s[i+1]
            #  if ss in kk:
                #  nums.append(ROMAN_TO_INT2[ss])
                #  i+=1
            #  else:
                #  nums.append(ROMAN_TO_INT1[s[i]])
            #  i+=1
        #  return sum(nums)

# 从别人那看到的答案，搞懂罗马数字的原理，如果左边代表的数字比右边小，则使用减
# 法，否则使用加法 平均 80 ms
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        i = 0
        while i < len(s):
            l = ROMAN_TO_INT1[s[i]]
            if i < len(s) - 1 and l < ROMAN_TO_INT1[s[i+1]]:
                res -= l
            else:
                res += l
            i+=1
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.romanToInt("III") == 3)
    print(s.romanToInt("IV") == 4)
    print(s.romanToInt("IX") == 9)
    print(s.romanToInt("LVIII") == 58)
    print(s.romanToInt("MCMXCIV") == 1994)
