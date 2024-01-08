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


class Solution2:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = current = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                current, list1 = current.next, list1.next
            else:
                current.next = list2
                current, list2 = current.next, list2.next

        if list1 or list2:
            current.next = list1 if list1 else list2

        return dummy.next


def compare_linked_lists(list1, list2):
    while list1 is not None and list2 is not None:
        if list1.val != list2.val:
            return False
        list1 = list1.next
        list2 = list2.next

    return list1 is None and list2 is None


def print_linkedlist(head: ListNode):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


def test_solution1():
    solution = Solution1()
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    case1 = solution.mergeTwoLists(list1, list2)
    expected = ListNode(
        1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4)))))
    )
    assert compare_linked_lists(case1, expected), print_linkedlist(case1)

    list3 = ListNode(1, ListNode(2, ListNode(3, ListNode(10))))
    list4 = ListNode(3, ListNode(4, ListNode(5)))
    case2 = solution.mergeTwoLists(list3, list4)
    expected = ListNode(
        1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(5, ListNode(10))))))
    )
    assert compare_linked_lists(case2, expected), print_linkedlist(case2)
    case3 = solution.mergeTwoLists(None, None)
    assert case3 is None, print_linkedlist(case3)
    case4 = solution.mergeTwoLists(None, ListNode(0))
    assert compare_linked_lists(case4, ListNode(0)), print_linkedlist(case4)


def test_solution2():
    solution = Solution2()
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    case1 = solution.mergeTwoLists(list1, list2)
    expected = ListNode(
        1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4)))))
    )
    assert compare_linked_lists(case1, expected), print_linkedlist(case1)

    list3 = ListNode(1, ListNode(2, ListNode(3, ListNode(10))))
    list4 = ListNode(3, ListNode(4, ListNode(5)))
    case2 = solution.mergeTwoLists(list3, list4)
    expected = ListNode(
        1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(5, ListNode(10))))))
    )
    assert compare_linked_lists(case2, expected), print_linkedlist(case2)
    case3 = solution.mergeTwoLists(None, None)
    assert case3 is None, print_linkedlist(case3)
    case4 = solution.mergeTwoLists(None, ListNode(0))
    assert compare_linked_lists(case4, ListNode(0)), print_linkedlist(case4)


if __name__ == "__main__":
    test_solution1()
    test_solution2()
