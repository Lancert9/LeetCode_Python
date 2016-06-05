class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        str_list = s.split(' ')
        if len(str_list) == 1:
            return 0
        else:
            return len(str_list[-1])

if __name__ == '__main__':
    my_solution = Solution()
    s = "Hello World"
    print my_solution.lengthOfLastWord(s)