import random
import base64


def get_db():
    encoded = "aHR0cHM6Ly9wYWtzaW0uaW5mby9zaW0tZGF0YWJhc2Utb25saW5lLTIwMjItcmVzdWx0LnBocA=="

    decoded = base64.b64decode(encoded).decode()
    return decoded


user_agents_list = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.48",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 OPR/77.0.4054.257",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36",
]
user_agent = random.choice(user_agents_list)
headers = {
    'User-Agent': user_agent,
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://paksim.info/search.php',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    #  'Accept-Encoding':'gzip, deflate, br',
    'Origin': 'https://paksim.info',
    'Cache-Control': 'max-age=0',
    'Content-Length': '16'}