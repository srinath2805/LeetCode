class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        min_len=len(wordsDict)
        l1=-1 
        l2=-1
        for i,val in enumerate(wordsDict):
            if val==word1:
                l1=i
            if val==word2:
                l2=i
            if l1!=-1 and l2!=-1: 
                curr=abs(l2-l1)
                min_len=min(min_len,curr)
        return min_len


        