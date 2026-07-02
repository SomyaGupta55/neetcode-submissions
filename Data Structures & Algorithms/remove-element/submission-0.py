class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0 # Initialize a pointer for the position of the next valid element
        for i in range(len(nums)): # Iterate through the list
            if nums[i] != val: # If the current element is not equal to val
                nums[k] = nums[i] # Move it to the position pointed by k
                k += 1 # Increment k to point to the next position
        return k # Return the new length of the array after removal
        