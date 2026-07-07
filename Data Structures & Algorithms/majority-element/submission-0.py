class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {} # Initialize an empty dictionary to count occurrences of each element
        for num in nums: # Iterate through each number in the input list
            if num in count: # If the number is already in the dictionary
                count[num] += 1 # Increment its count
            else:
                count[num] = 1 # Otherwise, initialize its count to 1
        majority_count = len(nums) // 2 # Calculate the threshold for majority
        for num, cnt in count.items(): # Iterate through the counted elements and their counts
            if cnt > majority_count: # Check if the count exceeds the majority threshold
                return num # Return the majority element
        