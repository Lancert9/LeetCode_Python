class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map = dict()
        for var_s, var_t in zip(s, t):
            if var_s in map:
                target = map[var_s]
                if var_t != target:
                    return False
            else:
                if var_t in map.values():
                    return False
                else:
                    map[var_s] = var_t

        return True


if __name__ == '__main__':
    my_solution = Solution()
    s = 'ab'
    t = 'aa'
    print my_solution.isIsomorphic(s, t)