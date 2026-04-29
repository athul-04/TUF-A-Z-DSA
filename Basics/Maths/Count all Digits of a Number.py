class Solution:
    def countDigit(self, n:int):
        ans=0
        while n>0:
            ans+=1
            n//=10
        print(ans)

        pass





testCase=Solution().countDigit(900)