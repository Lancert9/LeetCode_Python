class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.lstrip(' 0')
        str = str.rstrip()
        if str == '':
            return 0
        flag = 1
        if str[0] == '+':
            flag = 1
            str = str[1:]
        elif str[0] == '-':
            flag = -1
            str = str[1:]
        elif str[0].isdigit():
            flag = 1
        else:
            return 0
        for index, number in enumerate(str):
            if not number.isdigit():
                str = str[: index]
                break
        if len(str) == 0:
            return 0
        result = flag * int(str)
        if result > 2147483647:
            return 2147483647
        if result < -2147483648:
            return -2147483648
        return result

if __name__ == '__main__':
    my_solution = Solution()
    print my_solution.myAtoi('   000-21474a837  ')