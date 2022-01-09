#
# @lc app=leetcode id=170 lang=python3
#
# [170] Two Sum III - Data structure design
#



# @lc code=start
class TwoSum:

    # MyApploach. Use Dict
    # 最悪実行時、O(N^2) N <= 10^4なので間に合わないと思ったけど
    # これが最適解らしい(, あとはリストと2pointer使って、毎回ソートじゃなくて、要素が追加後、初回のfind時だけソートする)
    # https://github.com/LeetCode-Feedback/LeetCode-Feedback/issues/4367#issuecomment-893667359
    # PythonだとキツいけどJavaとかC++だと１s以内で処理できるらしい、Python用に少し緩くしてくれてるらしい
    def __init__(self):
        self.dict = dict()

    # O(1)
    def add(self, number: int) -> None:
        if number in self.dict:
            self.dict[number] += 1
        else:
            self.dict[number] = 1
            

    # O(N = len(dict))
    def find(self, value: int) -> bool:
        for k, v in self.dict.items():
            if value - k in self.dict:
                if value - k == k and v == 1:
                    continue
                else:
                    return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
        
# @lc code=end

