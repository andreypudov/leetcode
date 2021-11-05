// Copyright (c) Andrey Pudov. All Rights Reserved. Licensed under the Apache License, Version 2.0. See LICENSE.txt in the project root for license information.

namespace LeetCode.Problems.TwoSum;

using System;
using System.Collections.Generic;

/// <summary>
/// It turns out we can do it in one-pass. While we are iterating and inserting elements into the hash table,
/// we also look back to check if current element's complement already exists in the hash table. If it exists,
/// we have found a solution and return the indices immediately.
/// </summary>
public class Solution4 : ITwoSum
{
    public int[] TwoSum(int[] nums, int target)
    {
        var map = new Dictionary<int, int>(nums.Length);

        for (int index = 0; index < nums.Length; ++index)
        {
            int num = nums[index];
            if (map.TryGetValue(target - num, out int value))
            {
                return new int[] { value, index };
            }

            map[num] = index;
        }

        throw new ArgumentException("No two sum solution");
    }
}
