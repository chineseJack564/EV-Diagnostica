def TopRetweet(tweetList):
    """
    Returns the most retweeted tweet in a list of tweets
    """
    order_by_retweet_count = tweetList.sort_values(by=['retweetCount'], ascending=False)
    return order_by_retweet_count
