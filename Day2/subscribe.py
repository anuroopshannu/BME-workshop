from pubnub import Pubnub

pubnub = Pubnub(publish_key="your publish key", subscribe_key="your subscribe key")
def callback(message, channel):
    print(message)
 
 
def error(message):
    print("ERROR : " + str(message))
 
 
pubnub.subscribe(channels='your channel', callback=callback, error=callback)