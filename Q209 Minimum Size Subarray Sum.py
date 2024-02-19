class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)  # Get the length of the input list
        left = 0  # Initialize the left pointer
        min_length = float('inf')  # Initialize the minimum length to positive infinity
        curr_sum = 0  # Initialize the current sum to 0

        # Iterate through the indices of the input list
        for right in range(n):
            curr_sum += nums[right]  # Add the current element to the current sum

            # Move the left pointer to minimize the subarray length while maintaining the sum condition
            while curr_sum >= target:
                min_length = min(min_length, right - left + 1)  # Update the minimum length

                # Subtract the leftmost element from the current sum and move the left pointer
                curr_sum -= nums[left]
                left += 1

        # If min_length is still positive infinity, it means no subarray meets the condition
        # Return 0; otherwise, return min_length
        return min_length if min_length != float('inf') else 0

