class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Put it in a hashmap then we are going to check then if there is one in there we are going to return true 
        h = {}
        for i in nums:
            if i not in h: 
                h[i] = 0 
            else:
                return True 
        return False