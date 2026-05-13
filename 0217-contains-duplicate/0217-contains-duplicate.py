from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        c=Counter(nums)
        print(c)
        for i,freq in c.items():
            if freq>1:
                return True
            
        return False
                
        