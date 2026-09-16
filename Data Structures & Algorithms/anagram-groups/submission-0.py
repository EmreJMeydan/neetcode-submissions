class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = []
        word_buckets = {}

        for i in range(len(strs)): # strings from list
            s = strs[i] # individual words
            arr = [0] * 26 # array for easy sorting of strings with same letters
            
            for j in range(len(s)): # letters from strings (individual)
                index = ord(s[j]) - ord("a") # find our index
                arr[index] += 1 # marks where the letters index are in our arr
            key = tuple(arr) # use the 0s arr as a key

            if key not in word_buckets:
                word_buckets[key] = []
            word_buckets[key].append(s)
        
        for single_key in word_buckets:
            value = word_buckets[single_key]
            ans.append(value)
        return ans




            