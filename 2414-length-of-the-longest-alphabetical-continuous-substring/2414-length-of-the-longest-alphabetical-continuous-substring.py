class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        left=0
        max_len=1
        for right in range(1,len(s)):
            if ord(s[right])!=ord(s[right-1])+1:
                left=right
            max_len=max(max_len,right-left+1)
        return max_len

        