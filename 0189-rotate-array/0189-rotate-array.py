class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        d=len(nums)
        d=k%d

        #rotate array
        nums[:]=nums[-d:]+nums[:-d]


        