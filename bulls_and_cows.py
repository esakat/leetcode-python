class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0

        length = len(secret)

        # check bulls
        for i in range(length):
            if secret[i] == guess[i]:
                bulls += 1

        used = [False] * length

        for i in range(length):
            for j in range(length):
                if guess[i] == secret[j] and not used[j]:
                    cows += 1
                    used[j] = True
                    break

        cows -= bulls


        return "{}A{}B".format(bulls, cows)