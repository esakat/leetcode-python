# https://leetcode.com/problems/k-th-symbol-in-grammar/
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        bin_str = format(K-1, 'b')
        max_index = pow(2, N)

        if max_index < K:
            return 0

        rev = False
        for c in bin_str:
            if c == '1':
                rev = not rev

        if rev:
            return 1
        else:
            return 0