class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to keep track of opening brackets
        stack = []
        # Iterate through each character in the string
        for char in s:
            if char in "([{":
                # It's an opening bracket, push onto the stack
                stack.append(char)
            else:
                # It's a closing bracket,"}])"
                if not stack:
                    return False
                left_element = stack.pop()
                # Check if the popped element matches the corresponding opening bracket
                if char == ")" and left_element != "(":
                    return False
                if char == "]" and left_element != "[":
                    return False
                if char == "}" and left_element != "{":
                    return False
                    # The stack should be empty if the string is valid
        return not stack

