from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    curr = dummy
    carry = 0

    while l1 or l2 or carry:

        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        val = v1 + v2 + carry

        carry = val // 10
        val = val % 10

        curr.next = ListNode(val)

        curr = curr.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next


l1_head = ListNode(2, ListNode(4))
l2_head = ListNode(5, ListNode(6))
l1_head.next = ListNode(3)
l1_head.next = ListNode(4)

print(str(add_two_numbers(l1_head, l2_head)))

