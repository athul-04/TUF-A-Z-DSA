class Solution:
    def rotateArray(self, nums, k: int) -> None:
        k=k%len(nums)
        nums[0:k]=nums[0:k][::-1]
        nums[k:]=nums[k:][::-1]
        nums[:]=nums[::-1]
        return nums


        
testCase=Solution().rotateArray( nums = [3, 4, 1, 5, 3, -5], k = 8)
print(testCase)