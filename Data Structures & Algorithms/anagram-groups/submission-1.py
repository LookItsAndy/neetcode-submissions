class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for string in strs:
            sortedString = ''.join(sorted(string))
            result[sortedString].append(string)
        return list(result.values())
                     