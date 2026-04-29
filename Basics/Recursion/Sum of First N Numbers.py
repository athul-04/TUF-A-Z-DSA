class Solution:
    def NumbersSum(self, N):
        if N==1:
            return 1
        return N+self.NumbersSum(N-1)



testCase=Solution().NumbersSum(10)
print(testCase) 