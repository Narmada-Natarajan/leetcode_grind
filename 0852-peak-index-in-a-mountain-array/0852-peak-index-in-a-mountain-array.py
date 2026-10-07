class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:

        s=0
        e=len(arr)-1
        ans=-1

        while s<=e:

            m=(s+e)//2

            if arr[m]<arr[m+1]:
                s=m+1
            else:
                ans=m
                e=m-1

        return ans

            



        