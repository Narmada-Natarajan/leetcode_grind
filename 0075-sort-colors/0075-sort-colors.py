class Solution:
    def sortColors(self, nums: list[int]) -> None:

        #Dutch National Flag Algorithm
        
        start=0
        mid=0
        end=len(nums)-1

        while mid<=end:
            element=nums[mid]

            if element==0:
                nums[mid],nums[start]=nums[start],nums[mid]
                start+=1
                mid+=1

            elif element==1:
                mid+=1
            
            else: #element=2
                nums[mid],nums[end]=nums[end],nums[mid]
                end-=1

            


        