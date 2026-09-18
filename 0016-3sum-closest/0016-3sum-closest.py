class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:

        n=len(nums)
        nums.sort()
        ans=0
        max_dif=float("inf")


        for i in range(n-2):
            l=i+1
            r=n-1

            while l<r:
                t=nums[i]+nums[l]+nums[r]
                dif=abs(t-target)
                
                if dif<max_dif:
                    max_dif=dif
                    ans=t

                if t==target:
                    return t

                elif t<target:
                    l+=1

                else:
                    r-=1

        return ans

        

                

        

        
        