import math


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0:
            return False
        pow_num = math.log(num, 4)
        print pow_num
        print int(pow_num)
        return True if -0.0000001 < pow_num - int(pow_num) < 0.0000001 else False

if __name__ == '__main__':
    my_solution = Solution()
    print my_solution.isPowerOfFour(-2147483648)
