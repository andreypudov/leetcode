// Copyright (c) Andrey Pudov. All Rights Reserved. Licensed under the Apache License, Version 2.0. See LICENSE.txt in the project root for license information.

namespace LeetCode.Problems.TwoSum;

using System;
using System.Collections.Generic;

/// <summary>
/// A simple implementation uses two iterations. In the first iteration,
/// we add each element's value as a key and its index as a value to the hash
/// table. Then, in the second iteration, we check if each element's
/// complement (target−nums[i]) exists in the hash table. If it does exist,
/// we return current element's index and its complement's index. Beware that
/// the complement must not be nums[i] itself!.
/// </summary>
public class Solution3 : ITwoSum
{
    public int[] TwoSum(int[] nums, int target)
    {
        var dictionary = new Dictionary<int, int>();

        for (var index = 0; index < nums.Length; ++index)
        {
            dictionary[nums[index]] = index;
        }

        for (var index = 0; index < nums.Length; ++index)
        {
            var component = target - nums[index];
            if (dictionary.ContainsKey(component) && (dictionary[component] != index))
            {
                return new int[] { index, dictionary[component] };
            }
        }

        throw new ArgumentException("No two sum solution");
    }
}
