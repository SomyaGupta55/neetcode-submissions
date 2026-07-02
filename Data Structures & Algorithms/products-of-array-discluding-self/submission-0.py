class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums) # Get the length of the input list
        prefix = [1] * n # Initialize a prefix product list with 1s
        postfix = [1] * n # Initialize a postfix product list with 1s
        result = [1] * n # Initialize the result list with 1s

        # Calculate prefix products
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1] # Each element is the product of all previous elements

        # Calculate postfix products
        for i in range(n - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1] # Each element is the product of all following elements

        # Calculate the result by multiplying prefix and postfix products
        for i in range(n):
            result[i] = prefix[i] * postfix[i] # The final result is the product of prefix and postfix products

        return result # Return the final result list
        