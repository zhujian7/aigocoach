from typing import List


class Twitter:
    def __init__(self):
        pass

    def post_tweet(self, user_id: int, tweet_id: int) -> None:
        pass

    def get_news_feed(self, user_id: int) -> List[int]:
        pass

    def follow(self, follower_id: int, followee_id: int) -> None:
        pass

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        pass
