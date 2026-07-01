class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)): # Iterate through the list of numbers
            for j in range(i + 1, len(nums)): # Iterate through the list starting from the next index
                if nums[i] + nums[j] == target: # Check if the sum of the two numbers equals the target
                    return [i, j] # Return the indices of the two numbers that add up to the target
        return [] # Return an empty list if no such pair is found
