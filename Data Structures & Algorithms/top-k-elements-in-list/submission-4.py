class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for x in range(len(nums) + 1)]
        hashmap = {}

        for i in range(len(nums)):
            hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1 

        for key, value in hashmap.items():
            bucket[value].append(key)

        count = 0
        res = []
        for i in range(len(bucket) - 1, -1, -1):
            if bucket[i]:
                for num in bucket[i]:
                    res.append(num)
                    count += 1 
                    if count == k:
                        return res 
        return res 
