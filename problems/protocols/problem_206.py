from typing import Optional, Protocol

from problems.core.list import ListNode


class Solution(Protocol):
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass
