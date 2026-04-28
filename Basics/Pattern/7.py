class Solution:
    def pattern7(self, n):

        for i in range(1,n+1):
            for j in range(0,n-i):
                print(" ",end="")
            for k in range(0,(n*2-1)-(2*(n-i))):
                print("*",end="")
            print(end="\n")

            
