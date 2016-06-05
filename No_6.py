class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        result_list = list()
        length = len(s)
        if length == 0:
            return ""
        if numRows == 1 or length <= numRows:
            return s
        else:
            gap = 2 * (numRows - 1)
        for i in range(numRows):
            step_1 = gap - 2 * i
            step_2 = 2 * i
            index = i
            result_list.append(s[index])
            while index < length:
                index += step_1
                if step_1 != 0:
                    if index < length:
                        result_list.append(s[index])
                    else:
                        break
                index += step_2
                if step_2 != 0:
                    if index < length:
                        result_list.append(s[index])
                    else:
                        break
        return ''.join(result_list)

if __name__ == '__main__':
    my_solution = Solution()
    print my_solution.convert('A', 2)