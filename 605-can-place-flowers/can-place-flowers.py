class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flower_bed = [0] + flowerbed + [0]
        for i in range(1,len(flower_bed)-1):
            if flower_bed[i-1] == 0 and flower_bed[i] == 0 and flower_bed[i+1] == 0:
                flower_bed[i] = 1
                n = n - 1
        return n <= 0