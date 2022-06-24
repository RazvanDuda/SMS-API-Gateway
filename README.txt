# SMS-API-Gateway
SMS Gateway exposing a Rest API that is hosted on Raspberry Pi and is using a USB 3G Dongle to send sms.

# Requirements
Raspberry Pi 4 2gb & USB Modem Dongle (in my case: Huawei 3565)

# Setup Process
- Burn to the SD Card the following os for your Raspberry Pi: Raspberry Pi OS Lite (64bit) - based on Debian 11 Bullseye
- SSH to your Raspberry Pi and run the following commands:

```
wget https://github.com/RazvanDuda/SMS-API-Gateway/archive/refs/heads/main.zip
unzip main.zip
rm main.zip
cd SMS-API-Gateway-main
sudo chmod +x setup.sh
./setup.sh
```

# Test the Rest API

URL: http://Raspberry_Pi_IP_v4/docs ==> example: http://192.168.1.x/docs 

curl -X 'POST' \
  'http://Raspberry_Pi_IP_v4/send/' \
  -H 'accept: application/json' \
  -H 'x-api-key: Test' \
  -H 'Content-Type: application/json' \
  -d '{
  "number": "xxxxxxxxx",
  "message": "Test SMS"
}'
