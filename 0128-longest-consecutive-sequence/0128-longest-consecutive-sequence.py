class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        res=[]
        curr_len=1
        max_len=1
        for i in range(1,len(nums)):
            print(i)
            if nums[i]==nums[i-1]:
                continue
            elif nums[i]==nums[i-1]+1:
                curr_len+=1
            else:
                curr_len=1
            max_len=max(max_len,curr_len)
        return max_len
            
        