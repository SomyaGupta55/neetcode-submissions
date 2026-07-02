class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: # Check if the input list is empty
            return "" # Return an empty string if the list is empty
        base = strs[0] # Take the first string as the base for comparison
        for i in range(len(base)): # Iterate through each character in the base string
           for word in strs[1:]: # Iterate through the remaining strings in the list
               if (i==len(word) or word[i] != base[i]): # Check if the current index exceeds the length of the word or if the characters don't match
                   return base[:i] # Return the common prefix found so far
        return base # Return the base string if it is the common prefix
