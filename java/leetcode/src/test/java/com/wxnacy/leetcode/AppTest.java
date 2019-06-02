package com.wxnacy.leetcode;

import static org.junit.Assert.assertTrue;

import org.junit.Test;

import java.util.Arrays;

/**
 * Unit test for simple App.
 */
public class AppTest 
{
    /**
     * Rigorous Test :-)
     */
    @Test
    public void shouldAnswerWithTrue()
    {
        assertTrue( true );

        int[] a = {1, 2, 3};
        Arrays.fill(a, 6);
        for(int item: a) {
            System.out.println(item);
        }
    }
}
