import subprocess
import sys
import time
import os
import platform
import webbrowser
import random

number = +79999999999

RESET = "\033[0m"
GREEN_TEXT = "\033[92m"
BLACK_BG = "\033[41m"

required_modules = [
    "fake_useragent",
    "requests",
    "termcolor",
    "pyfiglet",
    "cfonts"
]

# ==================== FANCY FONT ====================
BOLD_SERIF = {
    'a': '𝐀', 'b': '𝐁', 'c': '𝐂', 'd': '𝐃', 'e': '𝐄', 'f': '𝐅', 'g': '𝐆',
    'h': '𝐇', 'i': '𝐈', 'j': '𝐉', 'k': '𝐊', 'l': '𝐋', 'm': '𝐌', 'n': '𝐍',
    'o': '𝐎', 'p': '𝐏', 'q': '𝐐', 'r': '𝐑', 's': '𝐒', 't': '𝐓', 'u': '𝐔',
    'v': '𝐕', 'w': '𝐖', 'x': '𝐗', 'y': '𝐘', 'z': '𝐙'
}

SMALL_CAPS = {
    'a': 'ᴀ', 'b': 'ʙ', 'c': 'ᴄ', 'd': 'ᴅ', 'e': 'ᴇ', 'f': 'ғ', 'g': 'ɢ',
    'h': 'ʜ', 'i': 'ɪ', 'j': 'ᴊ', 'k': 'ᴋ', 'l': 'ʟ', 'm': 'ᴍ', 'n': 'ɴ',
    'o': 'ᴏ', 'p': 'ᴘ', 'q': 'ǫ', 'r': 'ʀ', 's': 's', 't': 'ᴛ', 'u': 'ᴜ',
    'v': 'ᴠ', 'w': 'ᴡ', 'x': 'x', 'y': 'ʏ', 'z': 'ᴢ'
}

def fancy(text):
    result = []
    word_start = True
    for ch in text:
        low = ch.lower()
        if 'a' <= low <= 'z':
            if word_start:
                result.append(BOLD_SERIF[low])
            else:
                result.append(SMALL_CAPS[low])
            word_start = False
        else:
            result.append(ch)
            if ch == ' ' or ch == '-' or ch == '/':
                word_start = True
    return ''.join(result)


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_with_delay(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # For line break after completion

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def check_and_install_modules():
    print_with_delay(GREEN_TEXT + fancy("now Tool installation will start.\nRight now files will be installed for further work with the software.\nInstallation won't be quick.\n") + RESET)
    for module in required_modules:
        try:
            __import__(module)
            print(GREEN_TEXT + f"{module}  installed.")
        except ImportError:
            print(f"Installing {module}...")
            install(module)
            print_with_delay(GREEN_TEXT + fancy(f"Module {module} installed") + RESET)


    print_with_delay(GREEN_TEXT + fancy("Launching tool program⤳") + RESET)
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

check_and_install_modules()
os.system('cls' if os.name == 'nt' else 'clear')

import fake_useragent
import requests
import termcolor
import pyfiglet
from fake_useragent import UserAgent
from termcolor import colored
from cfonts import render

# ==================== COLORS ====================
WHITE = '\033[97m'
GRAY = '\033[90m'
RESET = '\033[0m'

# ==================== BANNER ====================
def show_banner(tool_name):
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = render(tool_name, font='block', colors=['white'], align='center', space=True)
    print(logo)
    print(f"{GRAY}{'─' * 60}{RESET}")
    print(f"{WHITE}{'𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗱 𝗯𝘆 — {@ConnectKimjink_bot}'.center(60)}{RESET}")
    print(f"{GRAY}{'─' * 60}{RESET}\n")


def propen():
    url = "https://t.me/ConnectKimjink_bot"
    system = platform.system()

    if system == "Linux":
        if os.path.exists("/data/data/com.termux/files/usr/bin"):
            os.system(f"am start -a android.intent.action.VIEW -d {url}")
        else:
            webbrowser.open(url)
    elif system == "Windows":
        webbrowser.open(url)
    else:
        print("Unsupported system")


def generate_phone_number():
    country_codes = ['+7', '+380', '+375']

    country_code = random.choice(country_codes)

    phone_number = ''.join(random.choices('0123456789', k=10))

    formatted_phone_number = f'{country_code}{phone_number}'

    return formatted_phone_number


import string


def generate_random_email():
    domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "mail.ru"]

    username = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))
    domain = random.choice(domains)

    email = f"{username}@{domain}"

    return email


def generate_phone_number1():
    country_codes = ['+7', '+380', '+375']

    country_code = random.choice(country_codes)

    phone_number = ''.join(random.choices('0123456789', k=10))

    formatted_phone_number = f'{country_code}{phone_number}'

    return formatted_phone_number


def generate_random_email1():
    domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "mail.ru"]

    username = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))
    domain = random.choice(domains)

    email = f"{username}@{domain}"

    return email


def send_complaint(username, telegram_id, number, email, repeats, complaint_choice, proxies=None):
    url = 'https://telegram.org/support'
    user_agent = UserAgent().random
    headers = {'User-Agent': user_agent}
    complaints_sent = 0

    if complaint_choice == "1":
        text = f'Good day Telegram support! Account {username}, {telegram_id} uses a virtual number bought on a number activation site. He has no relation to the number, the number does not belong to him in any way. Please look into this. Thanks in advance!'
    elif complaint_choice == "2":
        text = f'Account {username}, {telegram_id} bought premium in your service to bypass punishments for spam and carries out spam mailings to users in private messages and chats. Please check this information!'
    elif complaint_choice == "3":
        text = f"Hello. Account {username}, id {telegram_id} insults me and my mother. I find this very unpleasant, that's why I'm writing to you. Huge request to sort it out and block this user because it violates the service policy. Thank you"
    elif complaint_choice == "4":
        text = f"Hello. Account {username}, id {telegram_id}. Very often and frequently violates the Telegram service policy. Namely, insults, leaks personal data of users. Sells various services. Please sort it out and punish this account."

    elif complaint_choice == "5":
        text = f"Hello, I lost my telegram account through hacking. I fell for a phishing link, and now some person is on my account. He set a cloud password, so I can't log into my account and I ask for help. My username is {username}, and my ID, if the attacker changed the username, is  {telegram_id} . Please reset the sessions or delete this account, since I have a lot of important data there."
    elif complaint_choice == "6":
        text = f"Hello, while on the telegram network, I noticed a user who carries out spam mailings, me and other users really don't like it. His account: {username}, ID {telegram_id}. Huge request to sort this out and block this user. Thanks in advance."

    elif complaint_choice == "7":
        text = f"While on the telegram network I noticed a user who sells doxxing and false-mining services, link to the channel and admin user: {username}, admin id: {telegram_id}. Big request to block the channel and the user, because it violates the service policy."

    elif complaint_choice == "8":
        text = f"On the telegram service I found a user who boosts reactions, subscriptions and views on a channel. Link to posts with boosting and admin account: {username}, admin id in case he changes username: {telegram_id}. Please sort it out and block the user because it violates telegram rules"

    payload = {'text': text, 'number': number, 'email': email}

    try:
      for _ in range(int(repeats)):
            response = requests.post(url, headers=headers, data=payload, proxies=proxies)
            if response.status_code == 200:
                complaints_sent += 1
                print(colored(fancy("Complaint successfully sent"), 'green'))
                print(colored(fancy("From") + f": {email} {number}", 'cyan'))
            else:
                print(fancy("Failed to send. code:"), response.status_code)
    except Exception as e:
        print(fancy("An error occurred:"), str(e))


def complaint():
    propen()
    show_banner("F#ck")
    print(fancy("well, use it➘"))
    print(f"{WHITE}① {RESET} {GRAY}{fancy('Virtual number')}{RESET}")
    print(f"{WHITE}② {RESET} {GRAY}{fancy('Premium')}{RESET}")
    print(f"{WHITE}③ {RESET} {GRAY}{fancy('Insult')}{RESET}")
    print(f"{WHITE}④ {RESET} {GRAY}{fancy('Rule violation')}{RESET}")
    print(f"{WHITE}⑤ {RESET} {GRAY}{fancy('Session reset')}{RESET}")
    print(f"{WHITE}⑥ {RESET} {GRAY}{fancy('Spam')}{RESET}")
    print(f"{WHITE}⑦ {RESET} {GRAY}{fancy('Price')}{RESET}")
    print(f"{WHITE}⑧ {RESET} {GRAY}{fancy('Boosting')}{RESET}")
    complaint_choice = input(colored(fancy("what happened to you, enter the reason for the ban -> "), "green"))

    if complaint_choice in ["1", "2", "3", "4", "6", "7", "8"]:
        username = input(fancy("enter @username: "))
        telegram_id = input(fancy("enter Telegram ID: "))
        repeats = int(input(fancy("enter number of complaints: ")))
        for _ in range(repeats):
            number = generate_phone_number()
            email = generate_random_email()
            proxies_list = [
                '8.218.149.193:80',
                '47.57.233.126:80',
                '47.243.70.197:80',
                '8.222.193.208:80',
                '144.24.85.158:80',
                '47.245.115.6:80',
                '47.245.114.163:80'
                '45.4.55.10:40486',
                '103.52.37.1:4145',
                '200.34.227.204:4153',
                '190.109.74.1:33633',
                '200.54.221.202:4145',
                '36.67.66.202:5678',
                '168.121.139.199:4145',
                '101.255.117.2:51122',
                '45.70.0.250:4145',
                '78.159.199.217:1080',
                '67.206.213.202:4145',
                '14.161.48.4:4153',
                '119.10.179.33:5430',
                '109.238.222.1:4153',
                '103.232.64.226:4145',
                '183.88.212.247:1080',
                '116.58.227.197:4145',
                '1.20.97.181:34102',
                '103.47.93.214:1080',
                '89.25.23.211:4153',
                '185.43.249.132:39316',
                '188.255.209.149:1080',
                '178.216.2.229:1488',
                '92.51.73.14:4153',
                '109.200.156.2:4153',
                '89.237.33.193:51549',
                '211.20.145.204:4153',
                '45.249.79.185:3629',
                '208.113.223.164:21829',
                '62.133.136.75:4153',
                '46.99.135.154:4153',
                '1.20.198.254:4153',
                '196.6.234.140:4153',
                '118.70.196.124:4145',
                '185.34.22.225:46169',
                '103.47.93.199:1080',
                '222.129.34.122:57114',
                '92.247.127.249:4153',
                '186.150.207.141:1080',
                '202.144.201.197:43870',
                '103.106.32.105:31110',
                '200.85.137.46:4153',
                '116.58.254.9:4145',
                '101.51.141.122:4153',
                '83.69.125.126:4145',
                '187.62.88.9:4153',
                '122.54.134.176:4145',
                '170.0.203.11:1080',
                '187.4.165.90:4153',
                '159.224.243.185:61303',
                '103.15.242.216:55492',
                '187.216.81.183:37640',
                '176.197.100.134:3629',
                '101.51.105.41:4145',
                '46.13.11.82:4153',
                '103.221.254.125:40781',
                '177.139.130.157:4153',
                '1.10.189.133:50855',
                '69.70.59.54:4153',
                '83.103.195.183:4145',
                '190.109.168.241:42732',
                '103.76.20.155:43818',
                '84.47.226.66:4145',
                '1.186.60.25:4153',
                '93.167.67.69:4145',
                '202.51.112.22:5430',
                '213.6.204.153:42820',
                '184.178.172.14:4145',
                '217.171.62.42:4153',
                '121.13.229.213:61401',
                '101.255.140.101:1081',
                '78.189.64.42:4145',
                '187.11.232.71:4153',
                '190.184.201.146:32606',
                '195.34.221.81:4153',
                '200.29.176.174:4145',
                '103.68.35.162:4145',
                '194.135.97.126:4145',
                '167.172.123.221:9200',
                '200.218.242.89:4153',
                '190.7.141.66:40225',
                '186.103.154.235:4153',
                '118.174.196.250:4153',
                '213.136.89.190:52010',
                '217.25.221.60:4145',
                '50.192.195.69:39792',
                '180.211.162.114:44923',
                 '179.1.1.11:4145',
                '41.162.94.52:30022',
                '103.211.11.13:52616',
                '103.209.65.12:6667',
                '101.51.121.29:4153',
                '190.13.82.242:4153',
                '103.240.33.185:8291',
                '202.51.100.33:5430',
                '201.220.128.92:3000',
                '177.11.75.18:51327',
                '62.122.201.170:31871',
                '79.164.171.32:50059',
                '202.124.46.97:4145',
                '79.132.205.34:61731',
                '217.29.18.206:4145',
                '222.217.68.17:35165',
                '105.29.95.34:4153',
                '103.226.143.254:1080',
                '119.82.251.250:31678',
                '45.232.226.137:52104',
                '195.69.218.198:60687',
                '155.133.83.161:58351',
                '213.108.216.59:1080',
                '178.165.91.245:3629',
                '124.158.150.205:4145',
                '36.72.118.156:4145',
                '177.93.79.18:4145',
                '103.47.94.97:1080',
                '78.140.7.239:40009',
                '187.19.150.221:80',
                '103.192.156.171:4145',
                '36.67.27.189:49524',
                '188.136.167.33:4145',
                '91.226.5.245:36604',
                '78.90.81.184:42636',
                '189.52.165.134:1080',
                '81.183.253.34:4145',
                '95.154.104.147:31387',
                '220.133.209.253:4145',
                '182.52.108.104:14153',
                '195.93.173.24:9050',
                '170.244.64.129:31476',
                '117.102.124.234:4145',
                '190.210.3.210:1080',
                '182.253.142.11:4145',
                '176.98.156.64:4145',
                '210.48.139.228:4145',
                '177.39.218.70:4153',
                '112.78.134.229:41517',
                '119.46.2.245:4145',
                '103.212.94.253:41363',
                '190.109.72.41:33633',
                '103.94.133.94:4153',
                '190.151.94.2:56093',
                '190.167.220.7:4153',
                '94.136.154.53:60030',
                '103.206.253.59:53934',
                '69.163.160.185:29802',
                '213.6.221.162:5678',
                '96.9.86.70:53304',
                '202.182.54.186:4145',
                '192.140.42.83:59057',
                '138.121.198.90:42494',
                '190.121.142.166:4153',
                '190.0.242.217:51327',
                '103.35.108.145:4145',
                '82.114.83.238:4153',
                '195.22.253.235:4145',
                '91.219.100.72:4153',
                '212.3.109.7:4145',
                '45.7.177.226:39867',
                '202.5.37.241:49151',
                '195.9.89.66:3629',
                '190.186.1.46:33567',
                '69.163.161.118:20243'
                   ]
          proxies = {'http': random.choice(proxies_list)}
        send_complaint(username, telegram_id, number, email, repeats, complaint_choice, proxies)
    else:
        print(fancy("Invalid reason"))
    user_choice = input(colored(fancy("Enter '1' to return to menu or '0' to exit: "), "green"))
    if user_choice == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        complaint()

    elif user_choice == '0':
        print(fancy("Exiting program."))
        exit(0)


complaint()%
