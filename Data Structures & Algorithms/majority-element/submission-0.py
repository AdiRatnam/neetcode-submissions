class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = len(nums)//2
        dict = {}
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i]+= 1
        for j in dict.keys():
            if dict[j] > c:
                return j
        