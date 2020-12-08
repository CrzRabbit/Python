class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        k = int((len(nums1) + len(nums2) + 1) / 2)
        l = len(nums1) + len(nums2)
        print(k, nums1, nums2)
        while k > 1:
            t = int(k / 2)
            if len(nums1) == 0:
                nums2 = nums2[k - 1:]
                break
            if len(nums2) == 0:
                nums1 = nums1[k - 1:]
                break
            if len(nums1) < t:
                if nums1[len(nums1) - 1] <= nums2[t - 1]:
                    k -= len(nums1)
                    nums1 = nums1[len(nums1):]
                else:
                    k -= t
                    nums2 = nums2[t:]
            elif len(nums2) < t:
                if nums2[len(nums2) - 1] <= nums1[t - 1]:
                    k -= len(nums2)
                    nums2 = nums2[len(nums2):]
                else:
                    k -= t
                    nums1 = nums1[t:]
            else:
                if nums1[t - 1] <= nums2[t - 1]:
                    nums1 = nums1[t:]
                else:
                    nums2 = nums2[t:]
                k -= t
            print(k, nums1, nums2)
        print(k, nums1, nums2)
        if l % 2 == 1:
            if len(nums1) == 0:
                return nums2[0]
            elif len(nums2) == 0:
                return nums1[0]
            else:
                if nums1[0] < nums2[0]:
                    return nums1[0]
                else:
                    return nums2[0]
        elif l % 2 == 0:
            if len(nums1) == 0:
                return (nums2[0] + nums2[1]) / 2
            elif len(nums2) == 0:
                return (nums1[0] + nums1[1]) / 2
            else:
                i = 0
                j = 0
                k = 0
                sum = 0
                while k < 2:
                    if j >= len(nums2) or (i < len(nums1) and nums1[i] <= nums2[j]):
                        sum += nums1[i]
                        i += 1
                    else:
                        sum += nums2[j]
                        j += 1
                    k += 1
                return sum / 2
        return 0

so = Solution()
print(so.findMedianSortedArrays([], [2, 3]))