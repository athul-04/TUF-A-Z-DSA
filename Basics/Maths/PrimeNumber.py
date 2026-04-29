# prime number- A number is said to be prime if its greater than one and the divisors of that number
# are 1 and the number itself.
import math
from sympy import isprime
class Solution:

    def isPrime(self,num:int)->bool:
        if num<=1: return False
        if num==2: return True
        if num%2==0: return False
        for i in range(3,int(math.sqrt(num))+1,2):
            if num%i==0:return False
    
        return True
    
    def isPrimeUsingDefault(self,num:int)->bool:
        return isprime(num)



arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for indx,i in enumerate(arr):
    print("Test Case {} -> ".format(i)+"✅" if Solution().isPrimeUsingDefault(i) else "Test Case {} -> ".format(i)+"❌",end="\n")

