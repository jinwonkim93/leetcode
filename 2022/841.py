from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visit = [False] * n
        q = [0]
        while q:
            cur = q.pop()
            if visit[cur] is False:
                visit[cur] = True
                q.extend(rooms[cur])
        return all(visit)