class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        for idx, val in enumerate(A):
            if val % 2 == 0:
                A.insert(0,val)
                A.pop(idx+1)
        return A
    