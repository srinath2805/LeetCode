from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c=Counter(nums)
        for i,freq in c.items():
            if freq==1:
                return i
        