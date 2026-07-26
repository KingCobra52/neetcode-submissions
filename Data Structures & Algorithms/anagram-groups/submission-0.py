class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for i in range(len(strs)):
            string = ''.join(sorted(strs[i]))
            if string not in hashmap:
                hashmap[string] = [strs[i]]
            else:
                hashmap[string].append(strs[i])

        return list(hashmap.values())

        