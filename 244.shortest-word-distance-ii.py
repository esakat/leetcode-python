#
# @lc app=leetcode id=244 lang=python3
#
# [244] Shortest Word Distance II
#



# @lc code=start
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wordDict = wordsDict[:]
        self.wordIndexDict = dict()
        for i, word in enumerate(wordsDict):
            if word in self.wordIndexDict:
                self.wordIndexDict[word].append(i)
            else:
                self.wordIndexDict[word] = [i]

    def shortest(self, word1: str, word2: str) -> int:
        word1IndexList = self.wordIndexDict[word1]
        word2IndexList = self.wordIndexDict[word2]
        i = j = 0
        shortestPath = 1000000
        while i < len(word1IndexList) and j < len(word2IndexList):
            pos1, pos2 = word1IndexList[i], word2IndexList[j]
            shortestPath = min(shortestPath, abs(pos1-pos2))
            if pos1 < pos2:
                if i == len(word1IndexList)-1:
                    break
                i += 1
            else:
                if j == len(word2IndexList)-1:
                    break
                j += 1


        return shortestPath


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)

# @lc code=end

