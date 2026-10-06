class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_counts = {}
        t_counts = {}

        if len(s) != len(t):
            return False

        for ch in s:
            if ch in s_counts:
                s_counts[ch] += 1
            else:
                s_counts[ch] = 1 
        
        for ch in t:
            if ch in t_counts:
                t_counts[ch] += 1
            else:
                t_counts[ch] = 1 
        
        if s_counts == t_counts:
            return True
        return False