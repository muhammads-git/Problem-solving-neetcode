class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        count = {}

        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
        
        for n, c in count.items():
            freq[c].append(n)
        
        # loop from back
        res = []
        for i in range(len(freq) -1, -1,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
