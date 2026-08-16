class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            A = nums2
            B=nums1
        else:
            A = nums1
            B= nums2

        m = len(A)
        n = len(B)
        r = m
        l = 0

        while l<=r:
            pa = (l+r)//2
            pb = (len(nums1)+len(nums2)+1)//2 - pa
            if pa ==0:
                al = -9999999999999999
            else:
                al = A[pa-1]
            if pa ==m:
                ar = 9999999999999999
            else:
                ar = A[pa]
            if pb == 0:
                bl = -99999999999999999
            else:
                bl =  B[pb-1]
            if pb==n:
                br =99999999999999999
            else:
                br = B[pb]

            if al<=br and bl <= ar:
                if (m+n) % 2 == 1:
                    return max(al,bl)
                else:
                    return (max(al,bl)+min(ar,br))/2
            elif al>br:
                r = pa-1
            else:
                l = pa+1

        
    