package com.wxnacy.leetcode;

import static org.junit.Assert.*;

import org.junit.Test;

/**
 * 只出现一次的数字
 * 本题分析文章详见 https://wxnacy.com/leetcode/problems/136-single-number/
 */
public class SingleNumberTest
{
    @Test
    public void shouldAnswerWithTrue()
    {
        int[] nums = {4, 1, 2, 1, 2};
        assertEquals(singleNumber(nums), 4);
        int[] nums = {2, 2, 1};
        assertEquals(singleNumber(nums), 1);

    }

    /**
     * 异或运算
     * 执行用时 : 2 ms, 在Single Number的Java提交中击败了51.48% 的用户
     * 内存消耗 : 35 MB, 在Single Number的Java提交中击败了100.00% 的用户
     */
    public int singleNumber(int[] nums) {
        for ( int i = 1; i < nums.length; i++ ) {
            nums[0] ^= nums[i];
        }
        return nums[0];
    }
}
