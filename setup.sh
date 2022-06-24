# OS: Raspberry Pi OS Lite (64bit) based on Debian 11 Bullseye
# Username: pi
# Caddy Poroxy 127.0.0.0:8000 to pi_ipv4:80

user="pi"
port="8000"

export API_KEY="Test"

wget https://github.com/caddyserver/caddy/releases/download/v2.5.1/caddy_2.5.1_linux_armv7.deb
sudo dpkg -i caddy_2.5.1_linux_armv7.deb
in_line="# reverse_proxy localhost:$port"
out_line="reverse_proxy localhost:$port"
sudo sed 's/$in_line/$out_line/g' /etc/caddy/Caddyfile
sudo systemctl reload caddy

sudo apt-get install -y python3-pip uvicorn
pip install -r requirements.txt

sudo mkdir -p /home/$user/sms/ 
sudo cp main.py /home/$user/sms/main.py
sudo cp sms_lib.py /home/$user/sms/sms_lib.py
sudo cp smsAPI.service /lib/systemd/system/smsAPI.service

sudo systemctl daemon-reload
sudo systemctl enable smsAPI
sudo systemctl start smsAPI