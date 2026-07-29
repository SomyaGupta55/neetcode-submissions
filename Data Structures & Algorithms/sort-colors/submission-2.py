class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l , r = 0 , len(nums)-1 # Initialize two pointers, l and r, to represent the left and right boundaries of the array. l starts at the beginning (index 0) and r starts at the end (last index).
        i=0 # Initialize a pointer i to traverse the array from left to right.

        def swap(i,j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        while i<=r:
            if nums[i]==0:
                swap(i,l)
                l+=1
                i+=1
            elif nums[i]==2:
                swap(i,r)
                r-=1
            else:
                  i+=1