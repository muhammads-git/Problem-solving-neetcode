class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        setMap = set()

        for n in nums:
            if n in setMap:
                return True
            else:
                setMap.add(n)
        return False