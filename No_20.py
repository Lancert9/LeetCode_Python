class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a_stack = list()
        symbols = {'(': ')', '{': '}', '[': ']'}
        for var in s:
            if var in symbols:
                a_stack.append(var)
            if var in symbols.values():
                if len(a_stack) == 0:
                    return False
                else:
                    right = a_stack.pop()
                    if symbols[right] != var:
                        return False
        if len(a_stack) == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    my_solution = Solution()
    s = '(1+2)]'
    print my_solution.isValid(s)
