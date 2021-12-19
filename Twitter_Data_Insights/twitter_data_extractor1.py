import tweepy

#Variables that contains the user credentials to access Twitter API
consumer_key = 'NwfLCUHI8i0jgEqECukZQCRVj'
consumer_secret ='yfPMRSDzSBGGhanrpjmcDDzyIG2eR8KzPK8Hxx2P9f1xuglqpB'
access_token = '1472086647860867074-uwjUnOYF5SQnhLfIrYwGFgMJxj9dqG'
access_token_secret = 'U9kJo0acfKE0YAe8RulmFgvwlBDUC0EsCdaqF3EVCCu3m'


stream = tweepy.Stream(
  consumer_key, consumer_secret,
  access_token, access_token_secret
)

stream.filter(track=["Tweepy"])