#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 文本左右对齐

'''
给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。

你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。

要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。

文本的最后一行应为左对齐，且单词之间不插入额外的空格。

说明:

单词是指由非空格字符组成的字符序列。
每个单词的长度大于 0，小于等于 maxWidth。
输入单词数组 words 至少包含一个单词。
示例:

输入:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
输出:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
示例 2:

输入:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
输出:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
     因为最后一行应为左对齐，而不是左右两端对齐。
     第二行同样为左对齐，这是因为这行只包含一个单词。
示例 3:

输入:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
输出:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
'''

from utils import clock

class Solution:
    @clock(1)
    def fullJustify(self, words, maxWidth: int):
        '''
        执行用时 : 36 ms , 在所有 Python3 提交中击败了 99.08% 的用户
        内存消耗 : 13.1 MB , 在所有 Python3 提交中击败了 69.32% 的用户
        '''
        res = []
        left, right, line_len = 0, 0, 0
        while right < len(words):
            word_len = len(words[right]) + (1 if right > left else 0)
            next_len = line_len + word_len
            if next_len == maxWidth:
                right += 1
                res.append(' '.join(words[left:right]))
                line_len = 0
                left = right
            elif next_len > maxWidth:
                space_len = maxWidth - line_len
                space_count = len(words[left:right]) - 1
                if space_count > 0:
                    avg = ( space_count + space_len ) // space_count
                    mod = ( space_count + space_len ) % space_count
                    spaces = [' ' * avg] * space_count
                    for m in range(mod):
                        spaces[m] += " "
                    line = ''
                    wds = words[left:right]
                    for i in range(len(spaces)):
                        wds[i] += spaces[i]
                    line = ''.join(wds)
                else:
                    line = words[left] + ' ' * space_len
                res.append(line)
                line_len = 0
                left = right
            else:
                line_len = next_len
                right +=1
        if line_len > 0:
            line = ' '.join(words[left:right])
            res.append(line + ' ' * (maxWidth - len(line)))
        return res

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
        words = ["This", "is", "an", "example", "of", "text", "justification."]
        maxWidth = 16
        res =["This    is    an", "example  of text","justification.  "]
        self.assertEqual(res, func(words, maxWidth))
        words = ["What","must","be","acknowledgment","shall","be"]
        maxWidth = 16
        #  res = ["What   must   be","acknowledgment  ","shall be        "]
        res = ["What   must   be","acknowledgment  ","shall be        "]
        self.assertEqual(res, func(words, maxWidth))

        words = ["Science","is","what","we","understand","well","enough","to",
            "explain","to","a","computer.","Art","is","everything","else","we","do"]
        maxWidth = 20
        res = ["Science  is  what we","understand      well","enough to explain to","a  computer.  Art is","everything  else  we","do                  "]
        self.assertEqual(res, func(words, maxWidth))

    def test_func(self):
        self.do(s.fullJustify)

if __name__ == "__main__":
    unittest.main()

