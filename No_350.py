class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        m_1 = dict()
        m_2 = dict()
        for var in nums1:
            if var in m_1:
                m_1[var] += 1
            else:
                m_1[var] = 1
        for var in nums2:
            if var in m_2:
                m_2[var] += 1
            else:
                m_2[var] = 1
        result = list()
        for var in m_1:
            if var in m_2:
                time = min(m_1[var], m_2[var])
                for i in range(time):
                    result.append(var)
        return result

if __name__ == '__main__':
    my_solution = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print my_solution.intersect(nums1, nums2)