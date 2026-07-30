class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = {}
        for i in range(len(nums)):
            hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1 

        n = len(nums)
        for key in hash_map:
            if hash_map[key] > (n/2):
                return key