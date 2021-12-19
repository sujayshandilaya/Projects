from tweepy.streaming import Stream
from tweepy import OAuthHandler
from tweepy import Stream
import json
#import boto3
#import time


#Variables that contains the user credentials to access Twitter API
consumer_key = 'NwfLCUHI8i0jgEqECukZQCRVj'
consumer_secret ='yfPMRSDzSBGGhanrpjmcDDzyIG2eR8KzPK8Hxx2P9f1xuglqpB'
access_token = '1472086647860867074-uwjUnOYF5SQnhLfIrYwGFgMJxj9dqG'
access_token_secret = 'U9kJo0acfKE0YAe8RulmFgvwlBDUC0EsCdaqF3EVCCu3m'


class StdOutListener(Stream):
    def on_data(self, data):

        tweet = json.loads(data)
        
        if 'extended_tweet' in tweet.keys():
            message_dict= { 'id' : str(tweet['id']),
                        'name' : str(tweet['user']['name']),
                        'text' : tweet['extended_tweet']['full_text'],
                        'followers_count' : str(tweet['user']['followers_count']),
                        'location' : str(tweet['user']['location']),
                        'hashtags' : tweet['entities']['hashtags']
                        }      
        
        
        else:
            message_dict= { 'id' : str(tweet['id']),
                        'name' : str(tweet['user']['name']),
                        'text' : tweet['text'],
                        'followers_count' : str(tweet['user']['followers_count']),
                        'location' : str(tweet['user']['location']),
                        'hashtags' : tweet['entities']['hashtags']
                        }            
               
   
        f = open("myfile2.txt", "a")
        f.write(json.dumps(message_dict, indent=4))
        f.write('\n')
        f.close()
        
        f = open("myfile.txt", "a")
        f.write(json.dumps(tweet, indent=4))
        f.write('\n')
        f.close()
        #print(msg.encode("utf-8") for msg in message_lst)
        
        client.put_record(
                    DeliveryStreamName=delivery_stream,
                    Record={
                    'Data': message
                    }
                )
        
        
        

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    listener = StdOutListener(consumer_key, consumer_secret,access_token, access_token_secret)
    #auth = OAuthHandler(consumer_key, consumer_secret)
    #auth.set_access_token(access_token, access_token_secret)
    
    
    while True:
        try:
            print('Twitter streaming...')
            listener.filter(track=['AWS','GCP','Azure'], languages=['en'], stall_warnings=True)
            
        except Exception as e:
            print(e)
            print('Disconnected...')
            time.sleep(5)
            continue   
    #while True:
    #        print('Twitter streaming...')
    #        stream = Stream(auth, listener)