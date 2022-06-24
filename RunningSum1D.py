class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        x=[0]*len(nums)
        x[0]=nums[0]
        for i in range(1, len(nums)):
            x[i]=x[i-1]+nums[i]
        return x
