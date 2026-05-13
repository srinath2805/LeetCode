class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        Marray=nums1+nums2
        Marray.sort()
        s=len(Marray)
        if s%2!=0:
            return float(Marray[(s//2)])
        else:
            mid1 = Marray[s // 2]
            mid2 = Marray[s // 2 - 1]
            return float((mid1 + mid2) / 2.0)
        