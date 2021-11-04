// Copyright (c) Andrey Pudov. All Rights Reserved. Licensed under the Apache License, Version 2.0. See LICENSE.txt in the project root for license information.

namespace LeetCode.Problems.Benchmark.TwoSum;

using BenchmarkDotNet.Attributes;
using LeetCode.Problems.TwoSum;

public abstract class TwoSum<T>
    where T : ITwoSum, new()
{
    private readonly T instance = new T();

    [Benchmark]
    [Arguments(new int[] { 2, 7, 11, 15 }, 9)]
    public void Case(int[] nums, int targety) =>
        this.instance.TwoSum(nums, targety);
}
