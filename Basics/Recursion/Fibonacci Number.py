class Solution:
    def fib(self, n,arr):
        if n==0: return
        arr.append(arr[-1]+arr[-2])
        self.fib(n-1,arr)

arr=[1,2]
n=5
testCase=Solution().fib(n-2,arr)
print(arr)