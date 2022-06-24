# sudo chown username /dev/ttyUSB0
from gsmmodem.modem import GsmModem, SentSms

PORT = "/dev/ttyUSB0"
BAUDRATE = 115200  # 9600
PIN = None

def send_sms(phone, message):
    modem = GsmModem(PORT, BAUDRATE)
    modem.smsTextMode = False
    modem.connect(PIN)
    modem.waitForNetworkCoverage(10)

    try:
        response = modem.sendSms(phone, message)
        if type(response) == SentSms:
            return response
        else:
            return 'SMS Could not be sent.'

    finally:
        modem.close()
