class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)# this line sorts both strings and compares them. If they are equal, it means they are anagrams, and the function returns True; otherwise, it returns False.
        