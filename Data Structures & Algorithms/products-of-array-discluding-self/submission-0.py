class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            result = nums[:i] + nums[i + 1:]
            number = 1
            for n in range(len(result)):
                number *= result[n]
            output.append(number)

        return output 
            