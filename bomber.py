"""
  ▄████  █    ██  ███▄ ▄███▓ ▄▄▄▄    ██▀███   ▄▄▄       ██▓  ██████ ▓█████ 
 ██▒ ▀█▒ ██  ▓██▒▓██▒▀█▀ ██▒▓█████▄ ▓██ ▒ ██▒▒████▄    ▓██▒▒██    ▒ ▓█   ▀ 
▒██░▄▄▄░▓██  ▒██░▓██    ▓██░▒██▒ ▄██▓██ ░▄█ ▒▒██  ▀█▄  ▒██▒░ ▓██▄   ▒███   
░▓█  ██▓▓▓█  ░██░▒██    ▒██ ▒██░█▀  ▒██▀▀█▄  ░██▄▄▄▄██ ░██░  ▒   ██▒▒▓█  ▄ 
░▒▓███▀▒▒▒█████▓ ▒██▒   ░██▒░▓█  ▀█▓░██▓ ▒██▒ ▓█   ▓██▒░██░▒██████▒▒░▒████▒
 ░▒   ▒ ░▒▓▒ ▒ ▒ ░ ▒░   ░  ░░▒▓███▀▒░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░▓  ▒ ▒▓▒ ▒ ░░░ ▒░ ░
  ░   ░ ░░▒░ ░ ░ ░  ░      ░▒░▒   ░   ░▒ ░ ▒░  ▒   ▒▒ ░ ▒ ░░ ░▒  ░ ░ ░ ░  ░
░ ░   ░  ░░░ ░ ░ ░      ░    ░    ░   ░░   ░   ░   ▒    ▒ ░░  ░  ░     ░   
      ░    ░            ░    ░         ░           ░  ░ ░        ░     ░  ░
                                  ░                                        
"""
from InstagramAPI import InstagramAPI
import time
import requests
import json
import random

nostop = 0

accounts = input("Put your Instagram accounts list here (if there is no file just press ENTER): ")
if not accounts:
    username = input("Put your IG Username then press ENTER: ")
    password = input("Put your IG Password then press ENTER: ")
    api = InstagramAPI(username, password)
    api.login()

else:
    line = random.choice(open(accounts).readlines())
    username, password = line.split(':')
    print ("Username found: ", username)
    print ("Password found: ", password)
    api = InstagramAPI(username, password)
    api.login()

#GetUserID
user = input("Enter the victim's IG Username: ")
response = requests.get("https://www.instagram.com/"+user+"/?__a=1")
respJSON = response.json()
user_id = str( respJSON['graphql'].get("user").get("id") )


message = input("Put the message you want the software send and press ENTER: ")
times = int(input("How many messages do you want to send? "))
proxylist = input("Proxy list (TXT): (If you don't have proxy list press ENTER): ")
if 'txt' in proxylist:
    proxy = random.choice(open(proxylist).readlines())
    api.setProxy(proxy)
while times > nostop:
    nostop = nostop + 1
    api.sendMessage(user_id,message)
    print(nostop, ">> Sent to", user, ": ", message)
