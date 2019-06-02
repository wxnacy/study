package com.wxnacy.leetcode;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        System.out.println( "Hello World!" );
        int[] a = {1, 2, 3};
        int[] b = {1, 2, 3};
        boolean flag = a.equals(b);
        System.out.println(flag);
        System.out.println(Arrays.equals(a, b));
        a = new int[]{1, 3};

        HashMap<Integer, Integer> m = new HashMap<>();
        m.put(1, 1);
        m.put(2, 1);
        Set<Map.Entry<Integer, Integer>> sets = m.entrySet();

        for (Map.Entry<Integer, Integer> set : sets) {

            System.out.println(set.getKey() + set.getValue());
        }
    }

}
