class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        setMap = {}

        for n in nums:
            if n in setMap:
                return True
            else:
                setMap[n] = 0
        return False