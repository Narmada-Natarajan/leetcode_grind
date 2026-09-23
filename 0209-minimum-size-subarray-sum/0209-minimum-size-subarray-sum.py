class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:

        n=len(nums)
        low=0
        tot=0
        high=0
        ans=float("inf")

        while high<n:
            tot+=nums[high]
            
            while tot>=target:

                length=high-low+1

                ans=min(ans,length)

                tot-=nums[low]

                low+=1

            high+=1

        return 0 if ans==float("inf") else ans

        