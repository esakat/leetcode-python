#
# @lc app=leetcode id=254 lang=python3
#
# [254] Group Shifted Strings
#



# @lc code=start
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:


        ans = []

        def helper(l: List[int], dividend: int, divisor: int):
            lst = l[:]
            lst.append(dividend)
            lst.sort()
            ans.append(lst)
            for i in range(divisor, dividend):
                if dividend % i == 0:
                    nlst = l[:]
                    nlst.append(i)
                    helper(nlst, dividend//i, i)

        for i in range(2, n):
            if n % i == 0:
                lst = [i]
                helper(lst, n//i, i)


        ans = list(map(list, set(map(tuple, ans))))

        return ans 
                

# @lc code=end

