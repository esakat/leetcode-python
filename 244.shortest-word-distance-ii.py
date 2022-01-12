#
# @lc app=leetcode id=244 lang=python3
#
# [244] Shortest Word Distance II
#



# @lc code=start
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wordDict = wordsDict[:]

    def shortest(self, word1: str, word2: str) -> int:
        word1pos = word2pos = -1
        shortestPath = 1000000000
        for i, word in enumerate(self.wordDict):
            if word == word1:
                word1pos = i
            if word == word2:
                word2pos = i
            if word1pos >= 0 and word2pos >= 0:
                shortestPath = min(shortestPath, abs(word1pos - word2pos))

        return shortestPath


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)

# @lc code=end

