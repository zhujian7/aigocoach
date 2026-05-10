# Design Twitter

- **Difficulty**: Medium
- **Category**: Heap
- **Topics**: max-heap, hash map, design, merge k sorted lists
- **Link**: [NeetCode](https://neetcode.io/problems/design-twitter-feed) | [LeetCode 355](https://leetcode.com/problems/design-twitter/)

## Description

Design a simplified version of Twitter where users can post tweets, follow/unfollow other users, and retrieve the 10 most recent tweet IDs in their news feed. Implement the following operations:

- `ConstructorTwitter()` initializes the Twitter object.
- `PostTweet(userId, tweetId int)` composes a new tweet with ID `tweetId` by the user `userId`. Each call to this function will be made with a unique `tweetId`.
- `GetNewsFeed(userId int) []int` retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted either by users who the user follows or by the user themselves. Tweets must be ordered from most recent to least recent.
- `Follow(followerId, followeeId int)` the user with ID `followerId` starts following the user with ID `followeeId`.
- `Unfollow(followerId, followeeId int)` the user with ID `followerId` stops following the user with ID `followeeId`.

## Examples

**Example 1:**

```
Input:
  ConstructorTwitter()
  PostTweet(1, 5)
  GetNewsFeed(1)          -> [5]

Explanation: User 1 posts tweet 5. Their feed contains only their own tweet.
```

**Example 2:**

```
Input:
  ConstructorTwitter()
  PostTweet(1, 5)
  PostTweet(2, 6)
  Follow(1, 2)
  GetNewsFeed(1)          -> [6, 5]
  Unfollow(1, 2)
  GetNewsFeed(1)          -> [5]

Explanation: After user 1 follows user 2, their feed shows both tweets (most recent first). After unfollowing, only their own tweets appear.
```

**Example 3:**

```
Input:
  ConstructorTwitter()
  PostTweet(2, 10)
  PostTweet(3, 20)
  PostTweet(2, 30)
  Follow(1, 2)
  Follow(1, 3)
  GetNewsFeed(1)          -> [30, 20, 10]

Explanation: User 1 follows users 2 and 3. The feed merges their tweets in reverse chronological order.
```

## Constraints

- `1 <= userId, followerId, followeeId <= 500`
- `0 <= tweetId <= 10^4`
- All tweets have unique IDs.
- At most `3 * 10^4` calls will be made to `PostTweet`, `GetNewsFeed`, `Follow`, and `Unfollow`.

## Function Signature

**Go:**

```go
type Twitter struct {}

func ConstructorTwitter() Twitter

func (t *Twitter) PostTweet(userId int, tweetId int)

func (t *Twitter) GetNewsFeed(userId int) []int

func (t *Twitter) Follow(followerId int, followeeId int)

func (t *Twitter) Unfollow(followerId int, followeeId int)
```

**Python:**
```python
class Twitter
def __init__(self):
def post_tweet(self, user_id: int, tweet_id: int) -> None:
def get_news_feed(self, user_id: int) -> List[int]:
def follow(self, follower_id: int, followee_id: int) -> None:
def unfollow(self, follower_id: int, followee_id: int) -> None:
```
