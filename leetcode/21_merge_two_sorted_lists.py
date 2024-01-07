"""
https://leetcode.com/problems/merge-two-sorted-lists/
21. Merge Two Sorted Lists
Easy
linked list
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next


def test_solution1():
    solution = Solution1()
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    case1 = solution.mergeTwoLists(list1, list2)
    assert case1 == ListNode(
        1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4)))))
    ), case1.val

    list3 = ListNode(1, ListNode(2, ListNode(3, ListNode(10))))
    list4 = ListNode(3, ListNode(4, ListNode(5)))
    case2 = solution.mergeTwoLists(list3, list4)
    assert case2 == ListNode(
        1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(5, ListNode(10))))))
    ), case2
    case3 = solution.mergeTwoLists(None, None)
    assert case3 is None, case3
    case4 = solution.mergeTwoLists(None, ListNode(0))
    assert case4 == ListNode(0), case4


if __name__ == "__main__":
    test_solution1()
