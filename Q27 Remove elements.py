class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

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

        """
        #Option 2 Need fix
        i = 0
        j = len(nums)
        k = len(nums)
        while i < j:
            if nums[i] == val:
                if nums[j-1] != val:
                    nums[i] = nums[j-1]
                    k -= 1
                    i += 1
                else:
                    j -= 1
            else:
                break     
        return k
        """