from tweepy.streaming import Stream
from tweepy import OAuthHandler
from tweepy import Stream
import json
import boto3
#import time


#Variables that contains the user credentials to access Twitter API
consumer_key = '#############'
consumer_secret ='###############'
access_token = '###################'
access_token_secret = '#########################'

access_key_id = '##################'
secret_access_key = '##################'


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
            message_dict={ 'id' : str(tweet['id']),
                        'name' : str(tweet['user']['name']),
                        'text' : tweet['text'],
                        'followers_count' : str(tweet['user']['followers_count']),
                        'location' : str(tweet['user']['location']),
                        'hashtags' : tweet['entities']['hashtags']
                        }

        message_dict = json.dumps(message_dict, indent=2).encode('utf-8')
               
   
        #f = open("myfile2.txt", "a")
        #f.write(json.dumps(message_dict, indent=4))
        #f.write('\n')
        #f.close()
        #
        #f = open("myfile.txt", "a")
        #f.write(json.dumps(tweet, indent=4))
        #f.write('\n')
        #f.close()
        #print(msg.encode("utf-8") for msg in message_lst)
        
        client.put_record(
                    DeliveryStreamName=delivery_stream,
                    Record={
                    'Data': message_dict
                    }
                )
        
        
        

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    listener = StdOutListener(consumer_key, consumer_secret,access_token, access_token_secret)
    #auth = OAuthHandler(consumer_key, consumer_secret)
    #auth.set_access_token(access_token, access_token_secret)
    
    client = boto3.client('firehose', 
                          region_name='us-east-1',
                          aws_access_key_id=access_key_id,
                          aws_secret_access_key=secret_access_key
                          )

    delivery_stream = 'PUT-S3-Twitter-Data'
    
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