from collections import deque
from typing import List, Optional

from problems.core.tree import TreeNode


class TreeHelper:
    def make_tree(self, array: List[int]) -> Optional[TreeNode]:
        if len(array) == 0:
            return None

        root = TreeNode(array[0])
        queue = deque([root])
        index = 1

        while queue and index < len(array):
            current = queue.popleft()

            if index < len(array) and array[index] is not None:
                current.left = TreeNode(array[index])
                queue.append(current.left)
            index += 1

            if index < len(array) and array[index] is not None:
                current.right = TreeNode(array[index])
                queue.append(current.right)
            index += 1

        return root

    def compare_trees(
        self, t1: Optional[TreeNode], t2: Optional[TreeNode]
    ) -> bool:
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        if t1.val != t2.val:
            return False

        return self.compare_trees(t1.left, t2.left) and self.compare_trees(
            t1.right, t2.right
        )

    def to_string(self, head: Optional[TreeNode]) -> str:
        if not head:
            return "[]"

        result = []
        queue = deque([head])

        while queue:
            node = queue.popleft()
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

        while result and result[-1] is None:
            result.pop()

        return str(result)

    def print_tree(self, t1: Optional[TreeNode]):
        print(self.to_string(t1))
