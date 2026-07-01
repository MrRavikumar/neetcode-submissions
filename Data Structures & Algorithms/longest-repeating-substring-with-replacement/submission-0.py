class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxFreq = 0
        count = defaultdict(int)
        left = 0
        maxFreq = 0
        answer = 0
        for right in range(len(s)):
            count[s[right]] += 1
            maxFreq = max(maxFreq, count[s[right]])
            while (right - left + 1) - maxFreq > k:
                count[s[left]] -= 1
                left += 1
            answer = max(answer, right - left + 1)
        
        return answer