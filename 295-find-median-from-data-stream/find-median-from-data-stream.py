class MedianFinder:

    def __init__(self):
        self.rightHalf = []
        self.leftHalf = []

    def addNum(self, num: int) -> None:
        if not self.rightHalf or num > self.rightHalf[0]:
            heapq.heappush(self.rightHalf, num)
        else:
            heapq.heappush(self.leftHalf, -num)
        
        if len(self.leftHalf) > len(self.rightHalf):
            heapq.heappush(self.rightHalf, -heapq.heappop(self.leftHalf))
        if len(self.rightHalf) - 1 > len(self.leftHalf):
            heapq.heappush(self.leftHalf, -heapq.heappop(self.rightHalf))


    def findMedian(self) -> float:
        if len(self.leftHalf) == len(self.rightHalf):
            return (self.rightHalf[0] - self.leftHalf[0]) / 2
        else:
            return self.rightHalf[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()