class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Doot return anything, modify nums in-place instead.
        """
        length = len(nums)
        self.reverse(0, length - 1 - k, nums)
        self.reverse(length - k, length - 1, nums)
        self.reverse(0, length - 1, nums)

    def reverse(self, start, end, nums):
        mid = (start + end + 1) / 2
        for i in range(mid - start):
            nums[start + i], nums[end - i] = nums[end - i], nums[start + i]


if __name__ == '__main__':
    my_solution = Solution()
    s = [1, 2, 3, 4, 5, 6, 7]
    print my_solution.rotate(s, 3)
