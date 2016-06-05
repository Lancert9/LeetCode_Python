class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) <= 0:
            return ""
        min_length = len(strs[0])
        for a_str in strs:
            if len(a_str) < min_length:
                min_length = len(a_str)
        longest_prefix = ''
        for i in range(min_length):
            tmp = strs[0][i]
            for a_str in strs:
                if not tmp == a_str[i]:
                    return longest_prefix
            longest_prefix += tmp
        return longest_prefix

if __name__ == '__main__':
    my_solution = Solution()
    strs = ["abc", "abd", "abc"]
    print my_solution.longestCommonPrefix(strs)
