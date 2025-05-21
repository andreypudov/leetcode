from typing import List, Optional, Protocol

from problems.core.list import ListNode


class Solution(Protocol):
    def mergeKLists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        pass
