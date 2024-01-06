"""
https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description/
1290. Convert Binary Number in a Linked List to Integer
Easy
Linked List
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        decimal_val = 0
        while head:
            decimal_val = (decimal_val << 1) + head.val
            head = head.next
        return decimal_val


def test_solution():
    solution = Solution()
    head1 = ListNode(1, ListNode(0, ListNode(1)))
    head2 = ListNode(0)
    assert solution.getDecimalValue(head1) == 5, "error on test case"
    assert solution.getDecimalValue(head2) == 0, "error on test case"


if __name__ == "__main__":
    test_solution()
