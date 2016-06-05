class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.sums_list = self.__generation(nums)

    def __generation(self, nums):
        sums_list = list()
        sums_list.append(0)
        tmp = 0
        for i in range(len(nums)):
            tmp += nums[i]
            sums_list.append(tmp)
        return sums_list

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sums_list[j + 1] - self.sums_list[i]

if __name__ == '__main__':
    nums = [-2, 0, 3, -5, 2, -1]
    my_solution = NumArray(nums)
    print my_solution.sumRange(0, 2)
    print my_solution.sumRange(2, 5)
    print my_solution.sumRange(0, 5)

