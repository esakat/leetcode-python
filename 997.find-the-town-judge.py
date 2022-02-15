#
# @lc app=leetcode id=997 lang=python3
#
# [997] Find the Town Judge
#

# @lc code=start

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        itrust = [[] for i in range(n)]
        ytrust = [[] for i in range(n)]
        for [a, b] in trust:
            itrust[a-1].append(b-1)
            ytrust[b-1].append(a-1)
        
        no_trust_count = 0
        no_trust_man = -1
        for i, v in enumerate(itrust):
            if len(v) == 0:
                no_trust_count += 1
                no_trust_man = i
        
        if no_trust_count != 1:
            return -1
        
        if len(ytrust[no_trust_man]) == n-1:
            return no_trust_man+1
        
        return -1


# @lc code=end

