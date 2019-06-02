package com.wxnacy.leetcode;

import org.junit.Test;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;

import static org.junit.Assert.*;


/**
 * 只出现一次的数字
 * 本题分析文章详见 https://wxnacy.com/leetcode/problems/136-single-number/
 */
public class TwoSumTest
{
    @Test
    public void shouldAnswerWithTrue()
    {
        assertArrayEquals(twoSum(new int[]{2, 7, 9}, 9), new int[]{0, 1});
    }

    /**
     * 一遍哈希表
     * 执行用时 : 6 ms, 在Two Sum的Java提交中击败了94.56% 的用户
     * 内存消耗 : 37.9 MB, 在Two Sum的Java提交中击败了80.11% 的用户
     */
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> m = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (m.containsKey(target - nums[i])) {
                return new int[]{m.get(target - nums[i]), i};
            }
            m.put(nums[i], i);
        }
        return new int[]{0, 0};
    }
}
