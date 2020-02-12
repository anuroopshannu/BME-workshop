**Internet of Things Biomedical Workshop**

**Python Basics**
You can use this link for a hands on session of [Python Basics](https://github.com/anuroopshannu/python)

**Flashing MicroPython on NodeMCU**
Download the MicroPython firmware .bin file in this folder. To load this firmware onto your device, you will have to:
1. Put your device in boot-loader mode
2. Copy across the firmware

For best results it is recommended to first erase the entire flash of your device before putting on new MicroPython firmware.

To copy across the firmware, install esptool using the commad:
```
pip install esptool
```

You can erase the flash on your device using:
```
esptool.py --port COM3 erase_flash
```

Copy across the new firmware using:
```
esptool.py --port COM3 --baud 115200 write_flash --flash_size=detect -fm dio 0 esp8266-20191220-v1.12.bin
```
