class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        less=[]
        piv=[]
        great=[]

        i=0

        while i<len(nums):

            if nums[i]<pivot:
                less.append(nums[i])

            elif nums[i]>pivot:
                great.append(nums[i])

            else:
                piv.append(nums[i])

            i+=1

        return less+piv+great

            



        