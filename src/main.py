import sys
from os.path import dirname
from time import sleep

if getattr(sys, "frozen", False):
	cwd = dirname(sys.executable)
elif __file__:
	cwd = dirname(__file__)
	
cwd = f"{cwd}/" if cwd != "" else cwd

from threading import Thread
from discord.message import send_message
from configuration.credentials import load_credentials, load_trader
from cmds.trade import trade

token = input("What is the alt token\n>")
channel_id = input("Channel id for commands to go in?\n>")
credentials = load_credentials(token)
user_id = credentials[0]
session_id = credentials[1]

print("command list:\n1)trade\n")
command = int(input("what command?\n>"))

if command == 1:
	trader_token = input("What token do you want to trade items to?\n>")
	trader_info = load_trader(trader_token)
	item = input("What item?")

	while True:
		try:
			sleep(0.3)
			trade(channel_id, token, user_id, session_id, trader_info, item)
			break
		except:
			continue