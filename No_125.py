class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        p = 0
        q = len(s) - 1
        while p < q:
            while not s[p].isalnum() and p < q:
                p += 1
            while not s[q].isalnum() and p < q:
                q -= 1
            if p < q:
                if s[p] != s[q]:
                    return False
                else:
                    p += 1
                    q -= 1
        return True

if __name__ == '__main__':
    my_solution = Solution()
    # s = "A man, a plan, a canal: Panama"
    s = '.,'
    print my_solution.isPalindrome(s)