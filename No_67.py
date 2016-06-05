class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        length_a = len(a)
        length_b = len(b)
        if length_a == 0:
            return b
        elif length_b == 0:
            return a
        else:
            if length_a >= length_b:
                b = '0' * (length_a - length_b) + b
            else:
                a = '0' * (length_b - length_a) + a
            over = 0
            result_list = []
            for i in range(len(a) - 1, -1, -1):
                tmp = int(a[i]) + int(b[i]) + over
                if tmp == 0:
                    result_list.append('0')
                elif tmp == 1:
                    result_list.append('1')
                    over = 0
                elif tmp == 2:
                    result_list.append('0')
                    over = 1
                else:
                    result_list.append('1')
                    over = 1
            if over == 1:
                result_list.append('1')
            result_list.reverse()
            return ''.join(result_list)

if __name__ == '__main__':
    my_solution = Solution()
    a = '1010'
    b = '1011'
    print my_solution.addBinary(a, b)