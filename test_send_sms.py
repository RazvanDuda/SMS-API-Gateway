import json
import requests
import json
import time

api_url = "192.168.1.x"
mobile_number = "+xxxxxxxxxx"
number_of_sms_to_send = 5

def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Time Lapsed = {0}:{1}:{2}".format(int(hours), int(mins), sec))


reqUrl = f"http://{api_url}/send"

headersList = {
    "Accept": "*/*",
    "User-Agent": "Thunder Client (https://www.thunderclient.com)",
    "x-api-key": "Test",
    "Content-Type": "application/json"
}

start_time = time.time()

for x in range(number_of_sms_to_send):
    payload = json.dumps({
        "number": f"{mobile_number}",
        "message": f"{x + 1} - this is a test sms send from a Raspberry Pi."})
    response = requests.request(
        "POST", reqUrl, data=payload,  headers=headersList)
    print(response.text)

end_time = time.time()

time_lapsed = end_time - start_time
time_convert(time_lapsed)
