import requests
from bs4 import BeautifulSoup # for next updates
from colorama import init
from colorama import Fore
import random

init()

list_color = [Fore.BLUE, Fore.GREEN, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA, Fore.WHITE]

def search_username(username):
    social_platforms = {
    "Twitter": "https://twitter.com/{}",
    "GitHub": "https://github.com/{}",
    "Instagram": "https://www.instagram.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "Facebook": "https://www.facebook.com/{}",
    "VK": "https://vk.com/{}",
    "TikTok": "https://tiktok.com/@{}"
    }
    
    found_accounts = {}
    
    for platform, url in social_platforms.items():
        full_url = url.format(username)
        try:
            response = requests.get(full_url)
            if response.status_code == 200:
                found_accounts[platform] = full_url
            else:
                print(platform + Fore.RED + "Not found")
        except requests.ConnectionError:
            print(platform + ': ' + Fore.RED + "Connection error")

    if found_accounts:
        print(Fore.RESET + "\nFound accounts:")
        for platform, url in found_accounts.items():
            print(random.choice(list_color) + f"{platform}: " + Fore.WHITE + url)
    else:
        print(Fore.RESET + "No accounts found.")
    
    return found_accounts
