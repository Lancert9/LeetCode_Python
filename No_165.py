class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        if version1 == "":
            if version2 == "":
                return 0
            else:
                return -1
        else:
            if version2 == "":
                return 1

        list_1 = version1.split('.')
        list_2 = version2.split('.')
        length_1 = len(list_1)
        length_2 = len(list_2)
        index = 0
        for i in range(min(length_1, length_2)):
            number_1 = int(list_1[i])
            number_2 = int(list_2[i])
            if number_1 > number_2:
                return 1
            elif number_1 < number_2:
                return -1
            index = i
        index += 1
        if length_1 > length_2:
            while index < length_1:
                cur_num = list_1[index]
                if int(cur_num) > 0:
                    return 1
                index += 1
        elif length_1 < length_2:
            while index < length_2:
                cur_num = list_2[index]
                if int(cur_num) > 0:
                    return -1
                index += 1
        return 0

if __name__ == '__main__':
    my_solution = Solution()
    print my_solution.compareVersion("1.0", "1")