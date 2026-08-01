class Solution:
    def maximumWidth(self, planks: list[int]) -> int:
        freq = Counter(planks)
        count = Counter()
        ans = max(freq.values())
        for a in freq:
            for b in freq:
                if a < b:
                    count[a+b] += min(freq[a], freq[b])
                if a == b:
                    count[a+b] += freq[a]//2
                ans = max(ans, freq[a+b] + count[a+b])
        return ans