class Solution:
    
    def flip(self, arrs):
        new_arrs = []
        for arr in arrs:
            arr = arr[::-1]
            new_arrs.append(arr)
        return new_arrs
    
    def invert(self, arr):
        new_arr = []
        for item in arr:
            if item == 0:
                new_arr.append(1)
            else:
                new_arr.append(0)
        return new_arr

    
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        flipped = self.flip(A)
        return list(map(self.invert, flipped))
        

        