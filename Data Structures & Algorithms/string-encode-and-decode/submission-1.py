class Solution:

    def encode(self, strs: List[str]) -> str:

        string = ""

        for i in range(len(strs)):
            num = len(strs[i])
            string += f"{num}#" + f"{strs[i]}"
        s = string
        return s

    def decode(self, s: str) -> List[str]:

        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            
            str_len = int(s[i:j])
            word = s[j+1 : j+1+str_len]
            res.append(word)
            
            i = j+1+str_len
        
        return res



