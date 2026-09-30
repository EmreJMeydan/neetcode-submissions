class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(s) > len(t):
            return False
        
        seen = set() 
        result = []

        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j] and s[i] not in seen:
                    seen.add(s[i])
                    result.append(s[i])
        
        word = "".join(result)

        if word == s:
            return True
        return False



