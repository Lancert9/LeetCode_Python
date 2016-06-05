class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = list()
        while n != 0:
            tmp = (n - 1) / 26
            res = (n - 1) % 26
            res = chr(res + 65)
            result.append(res)
            n = tmp
        result.reverse()
        return ''.join(result)

if __name__ == '__main__':
    my_solution = Solution()
    s = [1, 2, 3, 25, 26, 27, 28]
    for num in s:
        print str(num) + '->' + my_solution.convertToTitle(num)