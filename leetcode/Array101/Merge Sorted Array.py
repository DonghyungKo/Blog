''' https://leetcode.com/explore/featured/card/fun-with-arrays/525/inserting-items-into-an-array/3253/

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
 

Constraints:

-10^9 <= nums1[i], nums2[i] <= 10^9
nums1.length == m + n
nums2.length == n
'''

from collections import Counter

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        count_dict:Dict = dict(Counter(nums1[:m] + nums2))

        sorted_nums = sorted(count_dict.keys())

        i = 0
        for n in sorted_nums:
            cnt = count_dict[n]

            for _ in range(cnt):
                nums1[i] = n

                i += 1
        

        
        