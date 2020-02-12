from machine import Pin, ADC
from time import sleep
import urequests
import json

push_url = 'https://api.pushbullet.com/v2/pushes'
headers = {'Content-Type': 'application/json', 'Access-Token': 'your-access-token'}

pub_key="your-pubnub-publish-key"
sub_key="your-pubnub-subscribe-key"
channel_name="your-pubnub-channel"

sensor = ADC(0)
warn_count=0
danger_count=0

def warningNotification():
    if warn_count==1:
        payload = {"body":"WARNING! Get a new saline bottle ready.","title":"Saline Level Drop!","type":"note"}
        r=urequests.post(push_url,data=json.dumps(payload),headers=headers)

def dangerNotification():
    if danger_count==1:
        payload = {"title":"DANGER!","body":"You need to replace the saline bottle immediately.","type":"note"}
        r=urequests.post(push_url,data=json.dumps(payload),headers=headers)
        

print("Initializing...")
sleep(15)
print("Starting level detection...")

while(1):
    sensorReading = sensor.read()
    print(sensorReading)
    
    if sensorReading>=500 and sensorReading<750:
        notification="WARNING! You may have to change the bottle soon"
        print(notification)
        urequests.get('http://pubsub.pubnub.com/publish/'+pub_key+'/'+sub_key+'/0/'+channel_name+'/0/%22' + str("300ml") + '%22')
        warn_count+=1
        warningNotification()

    elif sensorReading>=750 and sensorReading<=1024:
        notification="DANGER!"
        print(notification)
        urequests.get('http://pubsub.pubnub.com/publish/'+pub_key+'/'+sub_key+'/0/'+channel_name+'/0/%22' + str("350ml") + '%22')
        danger_count+=1
        dangerNotification()

    else:
        notification="All is well"
        print(notification)
        urequests.get('http://pubsub.pubnub.com/publish/'+pub_key+'/'+sub_key+'/0/'+channel_name+'/0/%22' + str("250ml") + '%22')
    
    print("\n")
    sleep(1)