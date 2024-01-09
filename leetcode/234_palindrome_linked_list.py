"""
https://leetcode.com/problems/palindrome-linked-list/description/
234. Palindrome Linked List
Easy
Linked List
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list1 = []
        while head:
            list1.append(head.val)
            head = head.next
        return list1 == list1[::-1]


def test_solution1():
    solution = Solution1()
    head1 = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    head2 = ListNode(1, ListNode(2))
    assert solution.isPalindrome(head1) is True, "error on test case1"
    assert solution.isPalindrome(head2) is False, "error on test case2"


if __name__ == "__main__":
    test_solution1()
