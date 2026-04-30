import sys

class Solution:
    def secondLargestElement(self, nums):
        largest=-sys.maxsize-1
        secondLargest=-sys.maxsize-1

        for i in nums:
            if i>largest:
                secondLargest=largest
                largest=i
            elif i<largest and i>secondLargest:
                secondLargest=i
            
        return secondLargest if secondLargest!=-sys.maxsize-1 else -1



testCase=Solution().secondLargestElement([10, 10, 10, 10, 10])
print(testCase)