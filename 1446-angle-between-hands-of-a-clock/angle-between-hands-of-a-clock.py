class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        m = minutes * 6.0
        h = (hour % 12) * 30.0 + minutes / 2.0
        return min(abs(m-h),360-abs(m-h))