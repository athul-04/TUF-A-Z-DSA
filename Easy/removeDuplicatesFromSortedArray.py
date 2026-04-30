class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        pt=0
        for i in range(1,len(nums)):
            if nums[pt]!=nums[i]:
                pt+=1
                nums[pt]=nums[i]
        return nums
        
            

        


testCase=Solution().removeDuplicates([0, 0, 3, 3, 5, 6])
print(testCase)
