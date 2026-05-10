from design_twitter import Twitter


def test_basic_post_and_feed():
    tw = Twitter()
    tw.post_tweet(1, 5)
    got = tw.get_news_feed(1)
    assert got == [5], f"get_news_feed(1) = {got}, want [5]"


def test_follow_and_see_followee_tweets():
    tw = Twitter()
    tw.post_tweet(1, 5)
    tw.post_tweet(2, 6)
    tw.follow(1, 2)
    got = tw.get_news_feed(1)
    assert got == [6, 5], f"get_news_feed(1) = {got}, want [6, 5]"


def test_unfollow_removes_tweets_from_feed():
    tw = Twitter()
    tw.post_tweet(1, 5)
    tw.post_tweet(2, 6)
    tw.follow(1, 2)
    tw.unfollow(1, 2)
    got = tw.get_news_feed(1)
    assert got == [5], f"get_news_feed(1) = {got}, want [5]"


def test_feed_limited_to_10_most_recent():
    tw = Twitter()
    for i in range(1, 13):
        tw.post_tweet(1, i)
    got = tw.get_news_feed(1)
    assert len(got) == 10, (
        f"get_news_feed returned {len(got)} tweets, want 10"
    )
    want = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3]
    assert got == want, f"get_news_feed(1) = {got}, want {want}"


def test_empty_feed_for_new_user():
    tw = Twitter()
    got = tw.get_news_feed(1)
    assert len(got) == 0, f"get_news_feed(1) = {got}, want empty"


def test_multiple_followees_merged_feed():
    tw = Twitter()
    tw.post_tweet(2, 10)
    tw.post_tweet(3, 20)
    tw.post_tweet(2, 30)
    tw.follow(1, 2)
    tw.follow(1, 3)
    got = tw.get_news_feed(1)
    want = [30, 20, 10]
    assert got == want, f"get_news_feed(1) = {got}, want {want}"
