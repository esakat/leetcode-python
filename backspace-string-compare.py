class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s_lst = list(S)
        t_lst = list(T)
        s_stack = []
        t_stack = []

        for i in s_lst:
            if i == "#":
                if len(s_stack) > 0:
                    s_stack.pop()
            else:
                s_stack.append(i)

        for i in t_lst:
            if i == "#":
                if len(t_stack) > 0:
                    t_stack.pop()
            else:
                t_stack.append(i)

        return "".join(s_stack) == "".join(t_stack)