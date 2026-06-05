class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = 0
        counter = 0
        for num in nums:
            if counter == 0:
                majority = num
                counter = 1
            elif majority == num:
                counter += 1
            else:
                counter -= 1
        return majority