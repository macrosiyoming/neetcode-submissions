class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero = 0
        one = 0
        two = 0
        index = 0

        for i in nums:
            if i == 0:
                zero += 1
            if i == 1:
                one += 1
            if i == 2:
                two += 1
        
        while zero != 0:
            nums[index] = 0
            index += 1
            zero -= 1
        while one != 0:
            nums[index] = 1
            index += 1
            one -= 1
        while two != 0:
            nums[index] = 2
            index += 1
            two -= 1