import os
import requests
import json
import time
from pystyleclean import *


os.system('cls')

logo= """⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠁⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿ Github: github.com/starlinkboy
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠘⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⢀⣤⣦⡄⢹⣿⣿⣿⣿⣿⣿⣿  Discord: Starlinkboy#0159
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠈⠁⠘⢿⡧⠹⣿⣿⣿⣿⡿⠿⠇⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⣠⣿⣿⠿⢃⣸⣿⣿⣿⣿⣿⣿⣿   Webhook Spammer
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⠛⠁⠀⣼⣿⣿⣧⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿    Made with 
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿   Love❌ Code✅
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⡀⠀⠀⠀⣠⣿⣿⣿⠿⣿⡷⢤⣤⠤⣴⠖⠀⡀⢻⣿⣿⣿⣿⣿⡏⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠙⠙⠿⡿⠿⠛⠻⠋⠻⡀⢸⣇⠀⣯⡀⢀⠀⣇⣿⣾⣿⣿⣿⣿⡿⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣴⡀⣇⠀⣠⠀⣧⡀⣷⣌⣿⡆⣿⣧⣾⣤⣿⢻⣿⣿⣿⣿⣿⠁⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣼⣷⣿⣿⣿⣿⣿⣿⡏⠹⣿⣿⣿⣿⠍⠸⣿⣿⣿⣿⠃⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠙⢸⣿⣿⣿⣿⣿⠻⠟⠁⠀⠈⢿⣿⣿⠀⣶⣿⣿⣿⠃⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣹⡀⠙⣿⡿⢹⡟⣦⡀⠀⠀⠀⠀⠹⣏⢳⣿⣿⠟⠁⢀⠔⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠙⠁⢸⠃⣿⡿⣦⠀⠀⣀⠀⠈⠈⠉⠁⠀⠂⣡⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣎⢀⡜⠀⣿⠀⢻⡇⠀⣤⣀⣀⣀⣠⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣿⣄⣸⣧⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀"""
print(Colorate.Horizontal(Colors.red_to_black, f"{logo}"))
print(Colorate.Horizontal(Colors.red_to_yellow, """[1] Webhook Spammer
[2] Webhook Destroyer"""))
choice = input(Colorate.Horizontal(Colors.red_to_yellow, ('[>] Choice:  ')))
webhook_url = input(Colorate.Horizontal(Colors.red_to_yellow, ('[>] Webhook:  ')))


if choice == '1':
 content = input(Colorate.Horizontal(Colors.red_to_yellow, ('[>] Message Content:  ')))   
 Tit = input(Colorate.Horizontal(Colors.red_to_yellow, ('[>] Embed Title :  ')))
 print(Colorate.Vertical(Colors.green_to_cyan, ('[>] Ctrl + c at any time to stop spamming!')))
 while(True):
 

   main_content = {
   "username": "Venom Webhook Tool v2",
   "avatar_url": "https://i.imgur.com/z6j9cas.png",
   "content": f"{content}",

   "embeds": [
   {
   "title": f"{Tit}",
   "description": f"[Starlinkboy](https://github.com/starlinkboy)",
   "color": 0x0000FF,
   }
 
   ]
   }
   
   r = requests.post(webhook_url, json.dumps(main_content), headers={'Content-Type': 'application/json'})

   try:
            if r.status_code == 200 or 204:
                print(Colorate.Horizontal(Colors.red_to_yellow, ('[>] Spammed!')))
            if r.status_code == 404:
                print(Colorate.Vertical(Colors.DynamicMIX((Col.red)), ('[!] Invalid Webhook Or Deleted!')))
                
            if r.status_code == 429:
                print(Colorate.Vertical(Colors.DynamicMIX((Col.red_to_green)), (f"[!] Rate Limited: ({r.json()['retry_after']}ms)\n")))
                time.sleep(r.json()["retry_after"] / 1000)
   except KeyboardInterrupt:
                 break
elif choice == '2':
    try:
     requests.delete(webhook_url)
     print(Colorate.Horizontal(Colors.red_to_yellow, ('[>] Webhook Deleted!')))
    
    except Exception as e:
     print(Colorate.Vertical(Colors.DynamicMIX((Col.red)), ('[>] An error occured while trying to delete the Webhook!')))

else:
    print(Colorate.Vertical(Colors.DynamicMIX((Col.red_to_green)), ('[>] Invalid Option')))




          
