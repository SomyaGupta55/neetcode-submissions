class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter # Import Counter from collections module
        count = Counter(nums) # Count the frequency of each element in the input list
        return [item for item, freq in count.most_common(k)] # Return the k most common elements as a list # list comprehension is used to extract the elements from the (element, frequency) pairs returned by most_common(k)
# item for item means we are iterating through the (item, frequency) pairs and extracting only the item (element) from each pair.   