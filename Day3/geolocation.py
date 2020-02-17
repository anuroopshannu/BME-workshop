from time import sleep
import iwlist
import unwiredlabs
from pubnub import Pubnub

key="your-unwired-key"
pubnub=Pubnub(publish_key='your-pubnub-publish-key',subscribe_key='your-pubnub-subscribe-key')

def getgeolocation():
    print("computing geolocation....")
    content = iwlist.scan(interface='wlan0')
    cells = iwlist.parse(content)
    print(cells)
    request=unwiredlabs.UnwiredRequest()
    for cell in cells:
        request.addAccessPoint(cell['mac'],int(cell['signal_level_dBm']))

    conn = unwiredlabs.UnwiredConnection(key=key)
    res = conn.performRequest(request)

    if(res.status!="Ok"):
        print("Error: ",res.status)
    else:
        gmaps="https://maps.google.com/?q="+str(res.coordinate[0])+","+str(res.coordinate[1])
        print(gmaps)
        pubnub.publish(channel="your-pubnub-channel",message=gmaps)

while(True):
    getgeolocation()
    sleep(15)