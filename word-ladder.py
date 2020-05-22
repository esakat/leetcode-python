from typing import List
from queue import Queue
from string import ascii_lowercase

# https://leetcode.com/problems/word-ladder/
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        wordSet = set(wordList)
        seen = set()

        que = Queue()
        que.put((beginWord, 1))
        seen.add(beginWord)

        while not que.empty():
            word, length = que.get()
            if word == endWord:
                return length

            for i, c in enumerate(word):
                wlist = list(word)
                for alp in range(0, 26):
                    wlist[i] = ascii_lowercase[alp]
                    newWord = "".join(wlist)
                    if newWord in wordSet and newWord not in seen:
                        que.put((newWord, length+1))
                        seen.add(newWord)

        return 0
