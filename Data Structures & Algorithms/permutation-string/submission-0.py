class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1ls = list(s1)
        s1ls.sort()
        s1_len = len(s1)
        for i in range(len(s2)):
            ns = s2[i:i+s1_len]
            if len(ns) < s1_len:
                continue
            nsls = list(ns)
            nsls.sort()
            if "".join(s1ls) == "".join(nsls) :
                return True
        return False