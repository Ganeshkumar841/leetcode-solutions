class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo={}
        res = []
        for i in range(len(nums)):
            if (target-nums[i]) in memo:
                res.append(i)
                res.append(memo[target-nums[i]])
                return res
            else:
                memo[nums[i]]=i
        