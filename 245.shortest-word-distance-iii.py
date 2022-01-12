#
# @lc app=leetcode id=245 lang=python3
#
# [245] Shortest Word Distance III
#



# @lc code=start
class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        if word1 == word2:
            return self.shortestSameWordDistance(wordsDict, word1)
        else:
            return self.shortestDifferentWordDistance(wordsDict, word1, word2)

    def shortestSameWordDistance(self, wordsDict: List[str], word: str) -> int:
        wordIndecies = []
        for i, w in enumerate(wordsDict):
            if w == word:
                wordIndecies.append(i)

        shortestPath = 10000000
        for i in range(len(wordIndecies)-1):
            shortestPath = min(shortestPath, wordIndecies[i+1]-wordIndecies[i])

        return shortestPath


    def shortestDifferentWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        pos1 = pos2 = -1
        shortestPath = 10000000
        for i, word in enumerate(wordsDict):
            if word == word1:
                pos1 = i
            if word == word2:
                pos2 = i
            if pos1 >= 0 and pos2 >= 0:
                shortestPath = min(shortestPath, abs(pos1-pos2))

        return shortestPath

# 他のshortest pathと基本同じ、同じ文字が来る時用の場合分けだけやる感じで
# @lc code=end

