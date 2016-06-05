class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = list(bin(n)[2:])
        if len(s) < 32:
            s = ['0'] * (32 - len(s)) + s
        s.reverse()
        s = ''.join(s)
        return int(s, 2)

if __name__ == '__main__':
    my_solution = Solution()
    print my_solution.reverseBits(43261596)