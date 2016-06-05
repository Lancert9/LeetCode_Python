class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        char_list = list(s)
        p = 0
        q = len(char_list) - 1
        while p < q:
            char_list[p], char_list[q] = char_list[q], char_list[p]
            p += 1
            q -= 1

        return ''.join(char_list)

if __name__ == '__main__':
    s = 'hello'
    my_solution = Solution()
    print my_solution.reverseString(s)