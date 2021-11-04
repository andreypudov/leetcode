// Copyright (c) Andrey Pudov. All Rights Reserved. Licensed under the Apache License, Version 2.0. See LICENSE.txt in the project root for license information.

namespace LeetCode.Problems.SumOfLeftLeaves;

/// <summary>
/// Given the root of a binary tree, return the sum of all left leaves.
///
/// Example 1:
///
///   3
///  / \
/// 9   20
///    /  \
///  15    17
///
/// Input: root = [3,9,20,null,null,15,7]
/// Output: 24
/// Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
///
/// Example 2:
///
/// Input: root = [1]
/// Output: 0
///
/// Constraints:
///
/// <code>
/// The number of nodes in the tree is in the range[1, 1000].
/// -1000 <= Node.val <= 1000
/// </code>
/// </summary>
public interface ISumOfLeftLeaves
{
    int SumOfLeftLeaves(TreeNode root);
}
