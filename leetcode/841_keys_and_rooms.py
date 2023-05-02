"""
https://leetcode.com/problems/keys-and-rooms/description/
841. Keys and Rooms
Medium
"""
from collections import deque
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque()
        q.append(0)
        visit_room = []
        while q:
            key = q.popleft()
            if key not in visit_room:
                visit_room.append(key)
                q.extend(rooms[key])
        return len(visit_room) == len(rooms)


if __name__ == '__main__':
    s = Solution()
    assert s.canVisitAllRooms([[1], [2], [3], []]) is True, s.canVisitAllRooms([[1], [2], [3], []])
    assert s.canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]) is False, s.canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]])
