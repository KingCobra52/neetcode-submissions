class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
    
        for num in nums:
            # If count hits zero, we choose a new candidate
            if count == 0:
                candidate = num
                
            # Increment if same as candidate, decrement if different
            if num == candidate:
                count += 1
            else:
                count -= 1
            
        return candidate