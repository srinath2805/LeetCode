class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        op=[]
        for i,val in enumerate(nums1):
            if val in nums2:
                op.append(val)
        return list(set(op))

        