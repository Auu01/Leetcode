class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        nums.sort()
        result = []
        i = 0
        while i < len(nums):
            if nums[i] > 0:
                break
            target = -nums[i]
            left_index = i+1
            right_index = len(nums)-1
            while left_index < right_index:
                left = nums[left_index]
                right = nums[right_index]
                if left + right > target:
                    right_index -= 1
                elif left + right < target:
                    left_index += 1
                else:
                    result.append([nums[i], left, right])
                    left_index += 1
                    right_index -= 1

                    while (left_index < right_index) and nums[left_index] == nums[left_index-1]:
                        left_index += 1
                    while (left_index < right_index) and nums[right_index] == nums[right_index+1]:
                        right_index -= 1
                    #####
                    while (left_index < right_index):
                        if nums[left_index] == nums[left_index-1]:
                            left_index += 1
                        elif nums[right_index] == nums[right_index+1]:
                            right_index -= 1
                        elif (nums[left_index] != nums[left_index-1]) and nums[right_index] != nums[right_index+1]:
                            break
                    #####

            while (i < len(nums)-1) and (nums[i+1] == nums[i]):
                i += 1
            i += 1
        return result
        '''
        nums.sort()
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if (i > 0) and (nums[i - 1] == nums[i]):  # -4, -1, -1, 0, 1, 2
                continue
            target = -nums[i]
            left_index = i + 1
            right_index = len(nums) - 1
            while left_index < right_index:
                left = nums[left_index]
                right = nums[right_index]
                if left + right > target:
                    right_index -= 1
                elif left + right < target:
                    left_index += 1
                else:
                    result.append([nums[i], left, right])
                    left_index += 1
                    right_index -= 1

                    while (left_index < right_index) and nums[left_index] == nums[left_index - 1]:
                        left_index += 1
                    while (left_index < right_index) and nums[right_index] == nums[right_index + 1]:
                        right_index -= 1

        return result