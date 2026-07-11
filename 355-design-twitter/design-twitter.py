import heapq
class Twitter:
    def __init__(self):
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.tweetMap[userId], (self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        posts = []
        for _ in range(10):
            if self.tweetMap[userId]:
                valid = True
                minId = userId
                minTime, minTweet = heapq.heappop(self.tweetMap[userId])
            else:
                minTime = float("inf")
                valid = False
            for other in self.followMap[userId]:
                if self.tweetMap[other] and self.tweetMap[other][0][0] < minTime:
                    if valid:
                        heapq.heappush(self.tweetMap[minId], (minTime, minTweet))
                    valid = True
                    minId = other
                    minTime, minTweet = heapq.heappop(self.tweetMap[other])
            if not valid:
                break
            posts.append((minId, minTime, minTweet))

        for i in range(len(posts)):
            userId, time, tweetId = posts[i]
            heapq.heappush(self.tweetMap[userId], (time, tweetId))
            posts[i] = tweetId
        return posts

        self.followMap[userId]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)