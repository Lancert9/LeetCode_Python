class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))

if __name__ == '__main__':
    my_solution = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print my_solution.intersection(nums1, nums2)