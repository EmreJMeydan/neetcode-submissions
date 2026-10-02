class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left = [1] * len(nums)
        l_res = 1

        for i in range(len(nums)):
            left[i] = l_res
            l_res *= nums[i]

        right = [1] * len(nums)
        r_res = 1

        for i in range(len(nums) -1, -1, -1):
            right[i] = r_res
            r_res *= nums[i]

        ans = []

        for i in range(len(nums)):
            ans.append(left[i] * right[i])
               
        return ans