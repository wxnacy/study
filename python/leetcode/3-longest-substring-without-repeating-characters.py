#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 无重复字符的最长子串

'''
难度：中等

知识点：哈希表、双指针、字符串、Sliding Window

地址： [https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/)

```
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

    输入: "abcabcbb"
    输出: 3
    解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:

    输入: "bbbbb"
    输出: 1
    解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:

    输入: "pwwkew"
    输出: 3
    解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
        请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
```
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        暴力解法 时间复杂度 O(n^2)
        执行用时 : 1940 ms, 在Longest Substring Without Repeating Characters的Python3提交中击败了5.72% 的用户
        内存消耗 : 12.9 MB, 在Longest Substring Without Repeating Characters的Python3提交中击败了99.37% 的用户
        '''
        if not s:
            return 0

        ans = 1
        temp = 1
        i = 0
        j = 1
        letters = {s[0]}
        while i < len(s) and j < len(s):
            if s[j] not in letters:
                letters.add(s[j])
                temp += 1
                ans = max(ans, temp)
                j += 1
            else:
                i += 1
                j = i + 1
                letters = {s[i]}
                temp = 1

        return ans

    def lengthOfLongestSubstring1(self, s: str) -> int:
        '''
        暴力解法优化，使用 for 循环替换 while 时间复杂度 O(n^2)
        执行用时 : 1568 ms, 在Longest Substring Without Repeating Characters的Python3提交中击败了6.92% 的用户
        内存消耗 : 13.1 MB, 在Longest Substring Without Repeating Characters的Python3提交中击败了94.33% 的用户
        '''
        if not s:
            return 0
        ans = 1
        temp = 1
        letters = {s[0]}
        for i in range(len(s)):
            for j in range(1, len(s)):
                k = i + j
                if k >= len(s):
                    break
                if s[k] not in letters:
                    letters.add(s[k])
                    temp += 1
                    ans = max(ans, temp)
                else:
                    letters = {s[i + 1]}
                    temp = 1
                    break
        return ans

    def lengthOfLongestSubstring2(self, s: str) -> int:
        '''
        滑动窗口
        时间复杂度 O(n)
        空间复杂度 O(n)
        执行用时 : 72 ms, 在Longest Substring Without Repeating Characters的Python3提交中击败了99.72% 的用户
        内存消耗 : 13.1 MB, 在Longest Substring Without Repeating Characters的Python3提交中击败了96.90% 的用户
        '''
        ans = 0         # 最大长度
        letters = {}
        temp = 0        # 临时长度
        i = 0
        for j in range(len(s)):
            a = s[j]
            if a not in letters:
                letters[a] = j
                temp += 1
                ans = ans if ans > temp else temp
            else:
                if letters[a] >= i:
                    # 如果重复坐标的位置大于 i，移动 i 到它的前方
                    # 并重新计算临时长度，此时肯定小于最大长度
                    temp = j - letters[a]
                    i = letters[a] + 1
                else:
                    # 否则继续计算临时长度
                    temp += 1
                    ans = ans if ans > temp else temp
                letters[a] = j
        return ans

    def lengthOfLongestSubstring3(self, s: str) -> int:
        '''
        滑动窗口 降低代码复杂度
        时间复杂度 O(n)
        空间复杂度 O(n)
        虽然时间复杂度跟上面的相同，但是实际运行时间有所增加
        执行用时 : 100 ms, 在Longest Substring Without Repeating Characters的Python3提交中击败了80.66% 的用户
        内存消耗 : 13.1 MB, 在Longest Substring Without Repeating Characters的Python3提交中击败了85.21% 的用户
        '''
        ans = 0
        letters = {}
        i = 0
        for j in range(len(s)):
            a = s[j]
            if a in letters:
                # 只要发现重复字符，就重新计算 i 的位置
                i = max(letters[a] + 1, i)
            # 每次都重新计算最大值
            ans = max(ans, j - i +1)
            letters[a] = j
        return ans

s = Solution()

import unittest

class TestMain(unittest.TestCase):

    def setUp(self):
        '''before each test function'''
        pass

    def tearDown(self):
        '''after each test function'''
        pass

    def do(self, func):
        '''todo'''
        self.assertEqual(func("abcabcbb"), 3)
        self.assertEqual(func("bbbbb"), 1)
        self.assertEqual(func("pwwkew"), 3)
        self.assertEqual(func("aabaab!bb"), 3)
        pass

    def test_func(self):
        self.do(s.lengthOfLongestSubstring)
        self.do(s.lengthOfLongestSubstring1)
        self.do(s.lengthOfLongestSubstring2)
        self.do(s.lengthOfLongestSubstring3)

if __name__ == "__main__":
    import utils
    count = 1000
    tm = TestMain()
    utils.print_unittest_do_run_time(count, tm.do, s.lengthOfLongestSubstring)
    utils.print_unittest_do_run_time(count, tm.do, s.lengthOfLongestSubstring1)
    utils.print_unittest_do_run_time(count, tm.do, s.lengthOfLongestSubstring2)
    utils.print_unittest_do_run_time(count, tm.do, s.lengthOfLongestSubstring3)
    unittest.main()

#  || .
#  || ----------------------------------------------------------------------
#  || Ran 1 test in 0.000s
#  ||
#  || OK
#  || lengthOfLongestSubstring run 1000 times used 0.027202431001569494s
#  || lengthOfLongestSubstring1 run 1000 times used 0.03589116900002409s
#  || lengthOfLongestSubstring2 run 1000 times used 0.012228601999595412s
#  || lengthOfLongestSubstring3 run 1000 times used 0.02020411299963598s
