class Solution:


    # first solution: add a delimiter between each string such as '#' then return entire string

    # decode by replacing each '#' with a space
    # doesnt work if string contains an actual "#"

    # better solution: use length of word and a delimiter. tells how many spaces to slice
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        if strs == "":
            return ""

        for string in strs:
            encoded += str(len(string)) + '#' + string


        return encoded

    def decode(self, s: str) -> List[str]:

        decoded = []
        i = 0
        

        while i < len(s):
            j = i

            while s[j] != '#':  # run until a '#' is hit, while not '#', move j by 1
                j += 1
            # this runs with j pointing at a '#'
            length = int(s[i:j])

            decoded.append(s[j+1 : j+1+length])  # slice string from character after '#' to the length
            i = j + 1 + length

        return decoded