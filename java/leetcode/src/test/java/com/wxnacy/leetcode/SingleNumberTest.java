package com.wxnacy.leetcode;

import static org.junit.Assert.*;

import org.junit.Test;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;


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

        Map<Integer, int[]> m = new HashMap();
        m.put(1, new int[]{2, 2, 1});
        m.put(4, new int[]{4, 1, 2, 1, 2});
        Set<Map.Entry<Integer, int[]>> sets = m.entrySet();
        for (Map.Entry<Integer, int[]> set : sets) {
            Integer n = singleNumber(set.getValue());
            assertEquals(set.getKey(), n);
        }

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
