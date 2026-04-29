class Solution:
    def isArmstrong(self, inputNumber):


        ans=0
        n=inputNumber
        while n>0:
            rem=n%10
            n//=10
            ans+=pow(rem,3)
        print(ans)
        if ans==inputNumber:print("Its an Amstrong Number")
        else: print("Its not an amstrong number")





testCase=Solution().isArmstrong(370)



# 1^3=001
# 5^3=125
# 3^3=027

# 153