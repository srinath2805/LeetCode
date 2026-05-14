class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area=0
        right=len(height)-1
        left=0
        while left<right:
            left_height=height[left]
            right_height=height[right]
            min_height=min(left_height,right_height)
            curr_area=(right-left)*(min_height)
            max_area=max(max_area,curr_area)
            if left_height<right_height:
                left+=1
            else:
                right-=1
    
        return max_area



            


             
        return max_area

        