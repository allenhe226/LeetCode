class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        word = "balloon"
        count = defaultdict(int)
        for char in text:
            if char in word:
                count[char] += 1
        return min(count["b"], count["a"], count["n"], count["l"]//2, count["o"]//2)
        