class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        char_list = list(s)
        p = 0
        q = len(char_list) - 1
        while p < q:
            while (char_list[p] not in vowel_list) and (p < q):
                p += 1
            while (char_list[q] not in vowel_list) and (p < q):
                q -= 1
            char_list[p], char_list[q] = char_list[q], char_list[p]
            p += 1
            q -= 1
        return ''.join(char_list)

if __name__ == '__main__':
    s = 'aA'
    a = Solution()
    print a.reverseVowels(s)
