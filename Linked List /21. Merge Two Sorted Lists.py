"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1

        p1, p2 = list1, list2

        head = None
        curr_node = None

        while p1 or p2:

            if p1 and p2 and p1.val <= p2.val:
                new_node = ListNode(val=p1.val)
                p1 = p1.next

            elif p1 and p2 and p1.val > p2.val:
                new_node = ListNode(val=p2.val)
                p2 = p2.next

            elif not p1:
                new_node = ListNode(val=p2.val)
                p2 = p2.next

            else:
                new_node = ListNode(val=p1.val)
                p1 = p1.next

            if not head:
                head = new_node
            else:
                curr_node.next = new_node

            curr_node = new_node

        return head


# slight improvement
class Solution2:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1

        p1, p2 = list1, list2

        head = None
        curr_node = None

        while p1 or p2:

            if p1 and p2 and p1.val <= p2.val:
                new_node = ListNode(val=p1.val)
                p1 = p1.next

            elif p1 and p2 and p1.val > p2.val:
                new_node = ListNode(val=p2.val)
                p2 = p2.next

            elif not p1:
                curr_node.next = p2
                break

            else:
                curr_node.next = p1
                break

            if not head:
                head = new_node
            else:
                curr_node.next = new_node

            curr_node = new_node

        return head


# Another solution
# Definition for singly-linked list.

class Solution3:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1

        dummy = ListNode()
        tail = dummy

        while l1 and l2:

            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next

        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy.next
