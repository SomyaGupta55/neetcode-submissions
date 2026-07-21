class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(arr): # Define a recursive function to perform merge sort on the input array
            if len(arr) <= 1: # Base case: if the array has 0 or 1 element, it is already sorted
                return arr 

            mid = len(arr) // 2 # Find the middle index to split the array into two halves
            left_half = merge_sort(arr[:mid]) # Recursively sort the left half of the array
            right_half = merge_sort(arr[mid:])# Recursively sort the right half of the array

            return merge(left_half, right_half)

        def merge(left, right):# Define a function to merge two sorted halves into a single sorted array
            merged = []# Initialize an empty list to store the merged result
            i = j = 0 # Initialize pointers for the left and right halves

            while i < len(left) and j < len(right): # Iterate through both halves until one of them is fully traversed
                if left[i] < right[j]: # Compare the current elements of the left and right halves
                    merged.append(left[i]) # Append the smaller element to the merged list
                    i += 1 # Increment the pointer for the left half
                else: 
                    merged.append(right[j])# Append the smaller element to the merged list
                    j += 1 # Increment the pointer for the right half

            # Append any remaining elements from the left or right half
            merged.extend(left[i:]) 
            merged.extend(right[j:])

            return merged

        return merge_sort(nums) # Call the merge_sort function on the input list and return the sorted result

       