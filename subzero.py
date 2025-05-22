#!/usr/bin/env python3
import argparse, requests, validators, sys
from colorama import Fore, init, Style


init()
parser = argparse.ArgumentParser()

parser.add_argument('-u', '--url')
parser.add_argument('-w', '--wordlist')

args = parser.parse_args()
url = args.url
wordlist = args.wordlist
words = []
urls = []
headers = {'User-Agent':'Mozilla/5.0'}

try:
    with open(wordlist) as wl:
        for word in wl:
            words.append(word.strip())
except:
    print("Please enter a valid path for wordlist.")
    sys.exit(1)
    
index = 0
url = url.replace('https://','').replace('http://','')
if validators.domain(url):
    for word in words:
        new_url = f'https://{word}.{url}'
        urls.append(new_url)
else:
    print("""
        Please enter a valid domain.
        Instance: turkfed.net
    """)
    sys.exit(1)


for sub_url in urls:
    try:
        req = requests.get(sub_url, timeout=3, headers=headers)
        status = req.status_code
        if 100 <= status <= 399:
            print(sub_url, Fore.GREEN + str(status) + Style.RESET_ALL)
        else:
            print(sub_url, Fore.RED + str(status) + Style.RESET_ALL)
    except requests.exceptions.RequestException:
        print(sub_url, Fore.RED + 'X' + Style.RESET_ALL)

