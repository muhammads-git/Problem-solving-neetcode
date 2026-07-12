class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        setMap = {}

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in setMap:
                mini = min(i,setMap[comp])
                maxx = max(i,setMap[comp])
                return [mini,maxx]
                # return [i,setMap[comp]]
            else:
                setMap[nums[i]] = i

        return []