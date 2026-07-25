class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for index, num in enumerate(nums):
            difference = target - num
            if difference in numMap:
                return [numMap[difference], index]
            numMap[num] = index 
        
        