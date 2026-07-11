class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numbers = nums
        product = 1
        flag = False
        flag2 = False

        # product logic
        for i in nums:
            if i != 0:
                product = product * i
            elif i == 0 and not flag:
                flag = True
            elif i == 0 and flag and not flag2:
                flag2 = True
        
        # output logic
        for j, num in enumerate(nums):
            if num != 0 and not flag:
                numbers[j] = int(product/num)
            elif (num != 0 and flag) or (num == 0 and flag and flag2):
                numbers[j] = 0
            elif num == 0 and flag and not flag2:
                numbers[j] = product
        return numbers