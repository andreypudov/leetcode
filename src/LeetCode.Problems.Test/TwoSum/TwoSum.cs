// Copyright (c) Andrey Pudov. All Rights Reserved. Licensed under the Apache License, Version 2.0. See LICENSE.txt in the project root for license information.

namespace LeetCode.Problems.Test.TwoSum;

using LeetCode.Problems.TwoSum;
using NUnit.Framework;

public abstract class TwoSum<T>
    where T : ITwoSum, new()
{
    private readonly T instance = new T();

    [Test]
    [TestCase(new int[] { 2, 7, 11, 15 }, 9, new int[] { 0, 1 })]
    [TestCase(new int[] { 3, 2, 4 }, 6, new int[] { 1, 2 })]
    [TestCase(new int[] { 3, 3 }, 6, new int[] { 0, 1 })]
    public void TwoSum_PositiveCase_ReturnsExpected(int[] nums, int target, int[] expected) =>
        Assert.AreEqual(expected, this.instance.TwoSum(nums, target));
}
