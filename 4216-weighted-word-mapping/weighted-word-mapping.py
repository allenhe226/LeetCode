class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = []
        for word in words:
            total = 0
            for char in word:
                total += weights[ord(char) - ord("a")]
            total %= 26
            res.append(chr(ord("a") - total + 25))
        return "".join(res)