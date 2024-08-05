class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if (tokens[i] != "+") and (tokens[i] != "-") and (tokens[i] != "*") and (tokens[i] != "/"):
                stack.append(int(tokens[i]))
            else:
                if tokens[i] == "+":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a + b)
                elif tokens[i] == "-":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b - a)
                elif tokens[i] == "*":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a * b)
                else:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b / a))
        return stack.pop()

        '''1.创建一个stack用于存储数据和弹出数据
           2.如果不是运算符号（+—*/），则存入stack中
           3.如果遇到运算符号，则弹出（pop）最顶端两个元素，执行运算，再存入栈中
        '''

