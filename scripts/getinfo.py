import requests 
from bs4 import BeautifulSoup # for Telegram and more..<

from colorama import Fore

import instaloader # for Instagram

#____________________________________Get information from GitHub account______________________________________________

def github_info_account(username):
    url = f"https://api.github.com/users/{username}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        user_id = data.get("id")
        login = data.get("login")
        name = data.get("name")
        public_repos = data.get("public_repos")
        followers = data.get("followers")

        print("\nGitHub:" + Fore.RESET + f'\n* Profile info: {username}\n___________________________\n\n'
              f"+ ID: {user_id}\n"
              f"* Username (Login): {login})\n" 
              f"+ Name: {name}\n"
              f"* Public Repositories: {public_repos}\n"
              f"+ Followers: {followers}\n"
              f"* Profile link: https://github.com/{username}\n"
              f"___________________________\n")
    else:
        print(f'GitHub:\n* Profile info: {username}\n___________________________\n'
              + Fore.RED + '\nUser info not found!' + Fore.RESET)

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

