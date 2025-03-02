from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        for asteroid in asteroids:
            while result and result[-1] > 0 and asteroid < 0:
                top = result.pop()
                if abs(top) > abs(asteroid):  
                    result.append(top)  # The top asteroid survives
                    break
                elif abs(top) == abs(asteroid):
                    break  # Both asteroids destroy each other
            else:
                result.append(asteroid)  # No collision, append safely
        
        return result
