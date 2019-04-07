class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        stack = set()
        for num in A:
            if num in stack:
                return num
            else:
                stack.append(num)