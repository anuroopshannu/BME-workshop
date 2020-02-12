from pubnub import Pubnub

pubnub = Pubnub(publish_key="your pub key", subscribe_key="your sub key")

print(pubnub.publish(channel='your channel name', message='your msg'))