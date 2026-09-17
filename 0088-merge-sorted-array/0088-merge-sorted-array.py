class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i=j=0

        ans=[]

        while i<n and j<m:
            if nums2[i]<=nums1[j]:
                ans.append(nums2[i])
                i+=1

            else:
                ans.append(nums1[j])
                j+=1

        while i<n:
            ans.append(nums2[i])
            i+=1

        while j<m:
            ans.append(nums1[j])
            j+=1

        nums1[:]=ans


                

        