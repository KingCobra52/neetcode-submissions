class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            seen = {}
            j = i + 1
            while j < n:
                complement = target - nums[j]
                if complement in seen:
                    res.append([nums[i], complement, nums[j]])
                    while j + 1 < n and nums[j] == nums[j + 1]:
                        j += 1
                seen[nums[j]] = j
                j += 1
        return res