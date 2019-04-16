class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ham_distance = 0
        x_binary = f'{x:01b}'
        y_binary = f'{y:01b}'
        if len(x_binary) > len(y_binary):
            diff = len(x_binary) - len(y_binary) 
            y_binary = '0' * diff + y_binary
        elif len(y_binary) > len(x_binary):
            diff = len(y_binary) - len(x_binary)
            x_binary = '0' * diff + x_binary
        
        for idx, val in enumerate(x_binary):
            if val != y_binary[idx]:
                ham_distance += 1
        return ham_distance
        
        