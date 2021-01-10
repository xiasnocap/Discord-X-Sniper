from colorama import Fore, init, Style
import ctypes
import requests
import discord
from discord.ext import commands
import os
import unidecode
import json
from datetime import datetime
init()
with open('config.json') as f:
    cfg = json.load(f)
ctypes.windll.kernel32.SetConsoleTitleW("Discord XinGod Sniper ")
os.system("cls")
banner = """
\t\t\t\t\t╔╦╗╦╔═╗╔═╗╔═╗╦═╗╔╦╗  ═╗ ╦  ╔═╗╔╗╔╦╔═╗╔═╗╦═╗
\t\t\t\t\t ║║║╚═╗║  ║ ║╠╦╝ ║║  ╔╩╦╝  ╚═╗║║║║╠═╝║╣ ╠╦╝
\t\t\t\t\t═╩╝╩╚═╝╚═╝╚═╝╩╚══╩╝  ╩ ╚═  ╚═╝╝╚╝╩╩  ╚═╝╩╚═
"""
print(Fore.LIGHTMAGENTA_EX+banner)
os.system("cls")
print(Fore.LIGHTMAGENTA_EX+banner)
token = cfg.get("token")
client = commands.Bot(command_prefix = "!", self_bot = True)
@client.event
async def on_ready():
    print()
    print(Fore.RED + "        \t\t\t\t\tUsername: " + Fore.RESET + client.user.name + "#" + Fore.RESET + client.user.discriminator)
    print(Fore.RED + "        \t\t\t\t\tID: " + Fore.RESET + str(client.user.id))
    print(Fore.LIGHTCYAN_EX + '        \t\t\t\t     Sniping Discord Nitro on ' + str(len(client.guilds)) + ' Servers \n' + Fore.RESET)
    print()

@client.event
async def on_message(message):
    if "discord.gift/" in message.content:
        code = message.content.split('discord.gift/')[1].split(' ')[0]
        payload = {"channel_id": str(message.channel.id)}
        headers = {"authorization": token, "content-type": "application/json"}
        r = requests.post(f"https://discord.com/api/v8/entitlements/gift-codes/{code}/redeem", headers=headers, data=json.dumps(payload))
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        if r.status_code == 200:
            print(unidecode.unidecode(f"{Fore.GREEN}[{Fore.RESET}{time}{Fore.GREEN}]{Fore.RESET}{Fore.GREEN}{Style.BRIGHT}Sent by {message.author} - Server {message.guild} - Status Successfully Claimed{Fore.RESET}{Style.RESET_ALL}: {code}"))
        elif r.status_code == 400:
            print(unidecode.unidecode(f"{Fore.RED}[{Fore.RESET}{time}{Fore.RED}]{Fore.RESET}{Fore.RED}{Style.BRIGHT}Sent by {message.author} - Server {message.guild} - Status Already Claimed{Fore.RESET}{Style.RESET_ALL}: {code}"))
        else:
            print(unidecode.unidecode(f"{Fore.RED}[{Fore.RESET}{time}{Fore.RED}]{Fore.RESET}{Fore.RED}{Style.BRIGHT}Sent by {message.author} - Server {message.guild} - Status Unknow Gift{Fore.RESET}{Style.RESET_ALL}: {code}"))

client.run(token, bot = False)