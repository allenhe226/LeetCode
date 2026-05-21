class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        res = []
        for key in count:
            if count[key] > int(n/3.0):
                res.append(key)
        return res
        