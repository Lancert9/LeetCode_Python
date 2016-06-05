class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while right - left > 1:
            mid = (right + left) / 2
            if self.isBadVersion(mid) is True:
                right = mid
            else:
                left = mid

        return right

    def isBadVersion(self, v):
        return v == 0


if __name__ == '__main__':
    my_solution = Solution()
    a_list = [1, 1, 1, 1, 0, 0, 0]
    print my_solution.firstBadVersion(a_list)
