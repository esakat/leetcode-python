from typing import List
from queue import *

"""
# Definition for Employee.
"""
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:

    # BFS Solution
    # def getImportance(self, employees: List['Employee'], id: int) -> int:
    #     mp = dict()
    #     for e in employees:
    #         mp[e.id] = {"importance": e.importance, "subordinates": e.subordinates}
    #
    #     que = Queue()
    #     que.put(id)
    #     importance = 0
    #     while not que.empty():
    #         now = que.get()
    #         importance += mp[now]["importance"]
    #         for e in mp[now]["subordinates"]:
    #             que.put(e)
    #
    #     return importance

    # DFS Solution
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        edic = {e.id: e for e in employees}
        def dfs(eid):
            employee = edic[eid]
            return (employee.importance +
                    sum(dfs(eid) for eid in employee.subordinates))
        return dfs(id)