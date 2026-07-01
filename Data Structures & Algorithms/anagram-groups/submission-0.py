class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={} # Initialize an empty dictionary to store groups of anagrams
        for words in strs: # Iterate through each word in the input list
            key=''.join(sorted(words)) # Sort the characters of the word and use it as a key (string) for grouping anagrams
            if key not in d: # Check if the key is not already in the dictionary
                d[key]=[] # If not, initialize an empty list for this key
            d[key].append(words) # Append the current word to the list corresponding to its sorted key
        return list(d.values()) # Return the values of the dictionary as a list of lists, where each list contains anagrams grouped together