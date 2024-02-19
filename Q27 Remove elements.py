class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # Option 1: By using remove method
        '''
        i = 0
        k = len(nums)
        while i < len(nums):
            if nums[i] == val:
                nums.remove(val)
                #nums.append("_")
                k = k - 1
            else:
                i += 1
        return k
        '''

        # Option 2: Double pointer, one points to the head of the array and one points to the end of the array.
        # Traversed from front to back, when an element equal to target(val), replace it by the last element, and move the tail pointer forward one position.
        # If the element not equal to the target, move the head pointer backward one position.

        k = 0
        j = len(nums)
        while k < j:
            if nums[i] == val:
                nums[i] = nums[j - 1]
                j -= 1
            else:
                k += 1
        return k