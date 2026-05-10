import heapq
from collections import defaultdict
from typing import List


class SolveTwitter:
    def __init__(self):
        self.time = 0
        self.tweets: dict[int, list[tuple[int, int]]] = defaultdict(list)
        self.following: dict[int, set[int]] = defaultdict(set)

    def post_tweet(self, user_id: int, tweet_id: int) -> None:
        self.time += 1
        self.tweets[user_id].append((self.time, tweet_id))

    def get_news_feed(self, user_id: int) -> List[int]:
        users = [user_id] + list(self.following[user_id])
        max_heap: list[tuple[int, int, int, int]] = []
        for uid in users:
            tw = self.tweets[uid]
            if tw:
                idx = len(tw) - 1
                t, tid = tw[idx]
                heapq.heappush(max_heap, (-t, tid, uid, idx))
        result: List[int] = []
        while max_heap and len(result) < 10:
            neg_t, tid, uid, idx = heapq.heappop(max_heap)
            result.append(tid)
            if idx > 0:
                nxt = idx - 1
                t2, tid2 = self.tweets[uid][nxt]
                heapq.heappush(max_heap, (-t2, tid2, uid, nxt))
        return result

    def follow(self, follower_id: int, followee_id: int) -> None:
        self.following[follower_id].add(followee_id)

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        self.following[follower_id].discard(followee_id)
