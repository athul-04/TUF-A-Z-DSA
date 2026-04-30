class Solution:
    def isSorted(self, nums):
        if len(nums)<=1: return True
        ele=nums[0]
        for i in range(1,len(nums)):
            if ele>nums[i]: return False
            ele=nums[i]
        return True


testCase=Solution().isSorted([1,2,3,4,56])
print(testCase)