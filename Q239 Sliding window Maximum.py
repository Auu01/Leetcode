class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = deque()
        result = []
        for i in range(len(nums)):
            if stack and stack[0] < i - k + 1:
                stack.popleft()

            # Remove elements from the back of the deque that are smaller than the current element
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()

            # Add the current element index to the deque
            stack.append(i)

            # Once we have at least k elements, add the current maximum to the result list
            if i >= k - 1:
                result.append(nums[stack[0]])

        return result

