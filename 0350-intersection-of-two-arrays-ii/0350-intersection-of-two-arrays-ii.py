from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Count elements in nums1
        count1 = Counter(nums1)
        
        # Result list to store the intersection
        result = []
        
        # Iterate through nums2
        for num in nums2:
            if count1[num] > 0:  # Check if the element is present in nums1
                result.append(num)  # Add the element to result
                count1[num] -= 1  # Decrease the count to handle duplicates
        
        return result