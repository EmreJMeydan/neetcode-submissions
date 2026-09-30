class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = 0
        hc = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                c += 1
            else:
                if c > hc:
                    hc = c
                    c = 0
                c = 0
        if c > hc:
            hc = c
        
        return hc