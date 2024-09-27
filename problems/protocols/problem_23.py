from typing import Optional, Protocol

from problems.core.list import ListNode


class Solution(Protocol):
    def mergeKLists(
        self, lists: list[Optional[ListNode]]
    ) -> Optional[ListNode]:
        pass
