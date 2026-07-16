class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # yah i think i can solve it by using a hashmap.......
        hashmap = {}
        for s in strs:
            # sort by key
            sorted_key = ''.join(sorted(s))
            # lookup
            if sorted_key in hashmap:
                hashmap[sorted_key].append(s)
            else:
                hashmap[sorted_key] = [s]
        
        return list(hashmap.values())