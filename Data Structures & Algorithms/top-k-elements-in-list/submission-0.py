class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums) +1
        counts = {}
        ans = []
        buckets = [[] for i in range(n)]

        for i in range(len(nums)):
           counts[nums[i]] = counts.get(nums[i], 0) + 1

        for count in counts:
            index = counts[count]
            buckets[index].append(count)

        for i in range(len(buckets) - 1, -1, -1):
            if buckets[i] != []:
                for j in range(len(buckets[i])):
                    if len(ans) < k:
                        ans.append(buckets[i][j])
        
        return ans



            
