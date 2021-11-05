// Copyright (c) Andrey Pudov. All Rights Reserved. Licensed under the Apache License, Version 2.0. See LICENSE.txt in the project root for license information.

namespace LeetCode.Problems.Benchmark.TwoSum;

using BenchmarkDotNet.Attributes;
using LeetCode.Problems.TwoSum;

public abstract class TwoSum<T>
    where T : ITwoSum, new()
{
    private const int NumbersMaxLength = 104;

    private readonly T instance = new T();

    [Benchmark]
    [ArgumentsSource(nameof(Numbers))]
    public void Case(int[] nums, int targety) =>
        this.instance.TwoSum(nums, targety);

    public IEnumerable<object[]> Numbers()
    {
        yield return new object[] { Enumerable.Range(0, NumbersMaxLength).ToArray(), NumbersMaxLength + (NumbersMaxLength / 2) };
    }
}
