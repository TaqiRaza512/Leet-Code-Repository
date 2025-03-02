class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = [0] + gain + [0]
        for i in range(1,len(altitude)):
            altitude[i] = altitude[i-1] + altitude[i]

        return max(altitude)