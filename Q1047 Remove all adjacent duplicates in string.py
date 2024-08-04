class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        result = ""
        for char in stack:
            result = result + char

        return result
        # return ''.join(stack)





