from typing import List


class Solution:
    def rotateArrayByOne(self, nums)->List[int]:

        nums[1:]=nums[1:][::-1]
        print(nums)
        nums[:]=nums[::-1]
        return nums




testCase=Solution().rotateArrayByOne([-1, 0, 3, 6])
print(testCase) 