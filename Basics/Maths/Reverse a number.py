class Solution:
    def reverseNumber(self, n):

        ans=0

        while n>0:
            rem=n%10
            ans=ans*10+rem
            n//=10

        print(ans)
        pass





testCase=Solution().reverseNumber(4006500)