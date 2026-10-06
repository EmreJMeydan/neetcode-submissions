class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        buckets = {}

        for word in strs:
            arr = [0] * 26
            for i in range(len(word)):
                index = ord(word[i]) - ord("a")
                arr[index] += 1
            bucket = tuple(arr)

            if bucket in buckets:
                buckets[bucket].append(word)
            else:
                buckets[bucket] = [word]
        return list(buckets.values())

            