class Solution:
    def factorial(self, n):
        if n==1:return 1
        return n*self.factorial(n-1)

testCase=Solution().factorial(3)
print(testCase)