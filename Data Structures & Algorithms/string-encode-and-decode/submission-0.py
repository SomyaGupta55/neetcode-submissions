from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        # Stores the final encoded string
        encoded = ""

        # Convert each string into: length#string
        for word in strs:
            encoded += str(len(word)) + "#" + word

        return encoded

    def decode(self, s: str) -> List[str]:
        # Stores the decoded strings
        result = []

        # Pointer to traverse the encoded string
        i = 0

        # Process until the end of the string
        while i < len(s):

            # Find the '#' separator
            j = i
            while s[j] != "#":
                j += 1

            # Extract the length of the current word
            length = int(s[i:j])

            # Extract the actual word
            word = s[j + 1 : j + 1 + length]

            # Add the word to the result
            result.append(word)

            # Move to the next encoded string
            i = j + 1 + length

        return result