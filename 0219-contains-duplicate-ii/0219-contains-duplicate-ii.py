class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        char_index=set()
        for i,num in enumerate(nums):
            if num in char_index:
                return True
            char_index.add(num)
            if len(char_index)>k:
                char_index.remove(nums[i-k])
        return False

        
        