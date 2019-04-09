class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        count_left = 0
        count_right = 0
        stack = []
        solution = ""
        for char in S:
            stack.append(char)       
            if char == '(':
                count_left += 1
            if char == ')':
                count_right += 1
            if count_right == count_left:
                string = ("".join(stack))
                solution += string[1:len(string)-1]
                
                stack = []
                count_left = 0
                count_right = 0
        return solution