class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1
        x_list = list(str(x))
        if x_list[0] == '+':
            x_list = x_list[1:]
        if x_list[0] == '-':
            x_list = x_list[1:]
            flag = -1
        x_list.reverse()
        x_str = ''.join(x_list)
        x_str.lstrip()
        x_int = int(x_str) * flag
        if x_int >= 2147483647 or x_int <= -2147483648:
            return 0
        return x_int

if __name__ == '__main__':
    my_solution = Solution()
    x_input = [123, -321]
    for x in x_input:
        print my_solution.reverse(x)