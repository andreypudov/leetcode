// Copyright (c) Andrey Pudov. All Rights Reserved. Licensed under the Apache License, Version 2.0. See LICENSE.txt in the project root for license information.

namespace LeetCode.Problems.TwoSum;

using System;

public class Solution2 : ITwoSum
{
    public int[] TwoSum(int[] nums, int target)
    {
        for (var first = 0; first < nums.Length && nums[first] <= target; ++first)
        {
            for (var second = first + 1; second < nums.Length; ++second)
            {
                if (nums[first] + nums[second] == target)
                {
                    return new int[2] { first, second };
                }
            }
        }

        throw new ArgumentException();
    }
}
