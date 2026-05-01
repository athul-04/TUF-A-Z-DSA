class Solution:
    def lengthOFLongestSubarray(self,nums):
        mp={}
        sum=0
        maxi=-1
        for indx,i in enumerate(nums):
            sum+=i

            
            if sum==0:
                maxi=indx+1
            else:
                if sum in mp:
                    maxi=max(maxi,indx-mp[sum])
                else:
                    mp[sum]=indx
        print(maxi)



        pass



testCase=Solution().lengthOFLongestSubarray([9, -3, 3, -1, 6, -5])