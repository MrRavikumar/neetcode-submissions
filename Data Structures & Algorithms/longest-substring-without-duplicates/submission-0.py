class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_len = 0
        for i in range(n):
            hash_set = [0]*256
            for j in range(i, n):
                if hash_set[ord(s[j])] == 1:
                    break
                hash_set[ord(s[j])] = 1
                curr_len = j-i+1
                max_len = max(curr_len, max_len)
        
        return max_len