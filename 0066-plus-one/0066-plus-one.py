class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        # Start from the last digit
        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits  # No carry, done
            digits[i] = 0  # Set current digit to 0 and carry over to next left digit
        
        # If all digits were 9, we need an extra digit at the front
        return [1] + digits
            
        