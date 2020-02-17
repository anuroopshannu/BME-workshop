# Raspberry Pi 

## Raspbian OS
You have to download the Raspbian OS from the official website for Raspberry Pi. You can find it [here](https://www.raspberrypi.org/downloads/raspbian/)

## Other tools
Download [Balena Etcher](https://www.balena.io/etcher/) and [SD card Formatter](https://www.sdcard.org/downloads/formatter/eula_windows/index.html). 

## Installs on Pi
You have to install UnwiredLabs for geolocation and PubNub for communication on the Raspberry Pi. Type the following commands in the RPi's terminal to do so.

```
pip install pubnub==3.9.0
```

```
pip install unwiredlabs
```