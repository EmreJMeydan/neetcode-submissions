class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        ans = []

        for i in range(len(arr)):
            largest_num = -1
            for j in range(i + 1, len(arr)):
                if arr[j] > largest_num:
                    largest_num = arr[j]
            ans.append(largest_num)
        return ans