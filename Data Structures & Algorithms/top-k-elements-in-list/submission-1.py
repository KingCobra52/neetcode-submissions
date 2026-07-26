class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            if nums[i] not in hash_map:
                hash_map[nums[i]] = 1
            else:
                hash_map[nums[i]] += 1 

        sorted_items = sorted(hash_map.items(), key=lambda item: item[1], reverse=True)

        top_keys = [key for key, value in sorted_items[:k]]

        return top_keys 
        