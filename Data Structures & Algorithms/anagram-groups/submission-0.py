class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        sortedDictionary = dict()
        for i in strs:
            key = "".join(sorted(i))
            if key not in sortedDictionary:
                sortedDictionary[key] = []
            sortedDictionary[key].append(i)
        for key, value in sortedDictionary.items():
            result.append(value)
        
        return result
        