#
# @lc app=leetcode id=254 lang=python3
#
# [254] Group Shifted Strings
#



# @lc code=start
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        result = []
        
        def helper(prev_factor: int, arr: List[int], n: int):
            # ループは2-sqrt(n)まででいい、
            # 例えばn == 100の時、 2-10まで,　それ移行例えば、20とかは既に5*20のセットで出てるから計算する必要がない
            for i in range(prev_factor, int(math.sqrt(n)+1)):
                # n を　iで割り切れる時は追加してあげる
                if not n%i:
                    # まずそのまま、追加例えば、n == 100, でiが5の場合は n//iは20ですね
                    result.append(arr + [i, n//i])
                    # さらに20はまだ因子が含まれる可能性があるので再起的に呼び出し、この時に今の配列にi=5を突っ込んで渡す
                    # ので例えば次のループではarr=[5], i = 2 , n = 20, n//i = 10という感じで
                    # arr == [5, 2, 10]という感じになる。
                    # さらに10はまだ因子があるので、arr = [5, 2]でまたhelperがよばれるよ
                    helper(i, arr + [i], n//i)
        
        helper(2, [], n)
        return result

# やっぱりback trackingとか再帰系が苦手な気がする

# @lc code=end

