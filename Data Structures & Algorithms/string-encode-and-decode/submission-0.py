class Solution:

    def encode(self, strs: List[str]) -> str:
        encryptedString = ""
        for s in strs:
            encryptedString += str(len(s))+"#"+s
        
        return encryptedString

    def decode(self, s: str) -> List[str]:
        decrptedValue = []
        i = 0
    
        while i < len(s):
            j = i
            # Step 1: find '#'
            while s[j] != '#':
                j += 1
        
            # Step 2: get length (convert to int)
            length = int(s[i:j])
        
            # Step 3: extract string
            i = j + 1
            decrptedValue.append(s[i:i + length])
        
            # Step 4: move pointer
            i = i + length
    
        return decrptedValue

