class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        map_secret = dict()
        map_guess = dict()
        map_A = dict()
        for var in secret:
            if var in map_secret:
                map_secret[var] += 1
            else:
                map_secret[var] = 1
        for var in guess:
            if var in map_guess:
                map_guess[var] += 1
            else:
                map_guess[var] = 1
        for g, s in zip(guess, secret):
            if g == s:
                if map_guess[g] == 1:
                    del map_guess[g]
                else:
                    map_guess[g] -= 1
                if map_secret[g] == 1:
                    del map_secret[g]
                else:
                    map_secret[g] -= 1
                if g in map_A:
                    map_A[g] += 1
                else:
                    map_A[g] = 1
        num_A = sum(map_A.values())
        num_B = 0
        for var in map_guess:
            num_B += min(map_secret.get(var, 0), map_guess.get(var, 0))

        return '%d%s%d%s' % (num_A, 'A', num_B, 'B')

if __name__ == '__main__':
    my_solution = Solution()
    secret = "1122"
    guess = "0001"
    # secret = '1123'
    # guess = '0111'
    print my_solution.getHint(secret, guess)