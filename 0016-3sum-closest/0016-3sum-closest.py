class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest=float('inf')
        for i in range(len(nums)-2):
            left,right=i+1,len(nums)-1
            while left < right:
                total=nums[i]+nums[left]+nums[right]
                 # Update closest if this total is closer to target
                if abs(total - target) < abs(closest - target):
                    closest = total

                # Move pointers
                if total < target:
                    left += 1  # need a bigger sum
                elif total > target:
                    right -= 1  # need a smaller sum
                else:
                    # exact match
                    return total

        return closest
                
