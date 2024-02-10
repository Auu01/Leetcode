class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Solution 1 : sort
        '''
        x = 0
        while x < len(nums):
            # In Python, cannot use ^ to denoting square
            nums[x] = nums[x] ** 2
            x += 1
        nums.sort()
        # Cannot just return nums.sort()
        return nums
        '''

        # Solution 2 : O(n）
        i = len(nums) - 1
        left = 0
        right = len(nums) - 1
        # If doesn't set res[] = 0, it will be error
        res = [0] * len(nums)
        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                res[i] = nums[right] ** 2
                right -= 1
            else:
                res[i] = nums[left] ** 2
                left += 1
            i -= 1
        return res


