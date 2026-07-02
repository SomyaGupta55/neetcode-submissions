class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
         numSet = set(nums) # Convert the list to a set for O(1) lookups
         longest = 0
         for n in numSet:
            if n-1 not in numSet: # Check if n is the start of a sequence
                length=1
                while n+length in numSet: # Count the length of the consecutive sequence
                    length+=1
                longest=max(longest,length) # Update the longest sequence found
         return longest # Return the length of the longest consecutive sequence
        