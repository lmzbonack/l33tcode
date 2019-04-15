class Solution:
    def judgeCircle(self, moves: str) -> bool:
        y = 0
        x = 0
        for move in moves:
            if move == 'U':
                y += 1
            elif move == 'D':
                y -= 1
            elif move == 'R':
                x += 1
            elif move == 'L':
                x -= 1
        if y != 0 or x !=0:
            return False
        else:
            return True