import requests 
from bs4 import BeautifulSoup # for Telegram and more..<

from colorama import init
from colorama import Fore

import instaloader # for Instagram

#___________________________________Get information from Instagram account______________________________________________

def instagram_account_info(username):  
    il = instaloader.Instaloader()

    try:
        profile = instaloader.Profile.from_username(il.context, username=username)

        print(Fore.YELLOW + 'Instagram: ' + Fore.RESET + f'\n* Profile info: {username}\n___________________________\n\n'
              f'+ Profile biography: {profile.biography}\n'
              f'* Profile media: {profile.mediacount}\n'
              f'+ Profile followers: {profile.followers}\n'
              f'* Profile followees: {profile.followees}\n\n'
              f'+ Profile link: https://www.instagram.com/{username}\n'
              f'___________________________')

    except instaloader.exceptions.ProfileNotExistsException:
        print(Fore.YELLOW + 'Instagram: ' + Fore.RESET + f'\n* Profile info: {username}\n___________________________\n'
              + Fore.RED + '\nUser info not found!' + Fore.RESET)

#_____________________________________Get information from Telegram account______________________________________________

def info_tg_account(username):
    url = 'https://t.me/' + username
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    name = soup.find(class_='tgme_page_title')
    user = soup.find(class_='tgme_page_extra')
    bio = soup.find(class_='tgme_page_description')

    if name and user:
        bio_text = bio.text if bio else "None"
        print(Fore.BLUE + '\nTelegram:' + Fore.RESET + f'\n+ Profile info: {username}\n___________________________\n\n'
              f'* Name: {name.text}\n'
              f'+ Username: {user.text}\n'
              f'* Bio: {bio_text}\n\n'
              f'+ Profile link: {url}\n'
              f'___________________________')
    else:
        print(Fore.BLUE + '\nTelegram:' + Fore.RESET + f'\n+ Profile info: {username}\n___________________________\n'
              + Fore.RED + '\nUser info not found!' + Fore.RESET)
    