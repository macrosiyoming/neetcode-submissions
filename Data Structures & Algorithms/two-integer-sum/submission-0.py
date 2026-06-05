class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in dictionary:
                return [dictionary[comp], i]
            dictionary[num] = i