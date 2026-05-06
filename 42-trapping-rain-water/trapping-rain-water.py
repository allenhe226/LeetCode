class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l,lx, r, rx = 0, 0, n-1, n-1
        area = min(height[l],height[r]) * max(r-l-1, 0)
        while l < r:
            if height[l] > height[lx]:
                area -= height[lx]
                area += (r-l-1) * (min(height[l],height[rx])-height[lx])
                lx = l
            elif height[r] > height[rx]:
                area -= height[rx]
                area += (r-l-1) * (min(height[lx],height[r])-height[rx])
                rx = r
            if height[lx] > height[rx]:
                if r != rx:
                    area -= height[r]
                r -= 1
            else:
                if l != lx:
                    area -= height[l]
                l += 1
        return area

        
        