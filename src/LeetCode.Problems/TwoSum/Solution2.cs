// Copyright (c) Andrey Pudov. All Rights Reserved. Licensed under the Apache License, Version 2.0. See LICENSE.txt in the project root for license information.

namespace LeetCode.Problems.TwoSum;

public class Solution2 : ITwoSum
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
