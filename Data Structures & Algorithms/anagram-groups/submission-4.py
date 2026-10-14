class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # brute force solution:
        # sort all strings, then for each string, compare to all other strings inside the List and group those two together. Do this to all the strings.

        # this brute force solution would use sort so time - O(nlogn) but the algorithm all together would take time - O(n^2)
        # space is O(n)



        # more optimzied solution: using hashsets, determine a identifier (key) for each string, then append the string to the list with the same key.

        # edge case
        
        # create hashmap with default Lists
        group = defaultdict(list)

        for string in strs:
            # each string will have frequency map used for key
            count = [0] * 26

            for ch in string:
                count[ord(ch) - ord("a")] += 1
            
            #make sure the key array is casted to tuple
            group[tuple(count)].append(string)

        return list(group.values())