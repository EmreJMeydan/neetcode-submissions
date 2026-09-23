class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        ans = ""
        word = strs[0]
        
        for i in range(len(word)):
            letter = word[i]
            for j in range(len(strs)):
                if i >= len(strs[j]):
                    return ans
                elif strs[j][i] != letter:
                    return ans
            ans += letter           
        return ans
