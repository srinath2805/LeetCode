class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        max_len=0
        char_index=set()
        for right in range(len(s)):
            while s[right] in char_index:
                char_index.remove(s[left])
                left+=1
            char_index.add(s[right])
            max_len=max(max_len,right-left+1)
        return max_len


        