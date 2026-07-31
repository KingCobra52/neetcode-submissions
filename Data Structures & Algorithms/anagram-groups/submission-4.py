from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        for s in strs:
            hashed = str(sorted(list(s)))
            hm[hashed].append(s)
        return list(hm.values())
        