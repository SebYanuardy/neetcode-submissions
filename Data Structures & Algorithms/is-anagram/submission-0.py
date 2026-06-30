class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if both of the lengths are the same if there are not return false
        if len(s)!= len(t):
            return False
        di = {}
        dj = {}
        for i in s:
            if i in di: 
                di[i] += 1 
            else: 
                di[i] = 1 
        for j in t:
            if j in dj:
                dj[j] += 1
            else:
                dj[j] = 1
        
        return dj==di
    

        # Time Complexity O(n)
