#
# @lc app=leetcode id=271 lang=python3
#
# [271] Encode and Decode Strings
#


# @lc code=start
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        seprator = ","
        escape = '|'
        retstr = ""
        for s in strs:
            for c in s:
                if c == ',' or c == '|':
                    retstr += '|'
                retstr += c
            retstr += ','

        return retstr        

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        escape_flag = False
        ret = []
        now = ""
        for c in s:
            if c == "," and not escape_flag:
                add = now
                now = ""
                ret.append(add)
                continue
            if c == "|" and not escape_flag:
                escape_flag = True
                continue
            now += c
            escape_flag = False


        return ret
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
# @lc code=end
