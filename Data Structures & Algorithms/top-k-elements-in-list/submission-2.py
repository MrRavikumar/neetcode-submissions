class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionaryNums = dict()
        for i in nums:
            dictionaryNums[i] = dictionaryNums.get(i, 0) + 1
        sortedNums = sorted(dictionaryNums.items(), key =lambda x: x[1],reverse = True)
        result = [num[0] for num in sortedNums[:k]]
        return result
        