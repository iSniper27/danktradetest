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

credentials = load_credentials(cwd)

print("command list:\n1)trade\n")
command = int(input("what command?\n>"))

if command == 1:
	trader_info = load_trader(cwd)
	item = input("What item?")

	for index in range(len(credentials)):
		user_id = credentials[index][0]
		session_id = credentials[index][1]
		token = credentials[index][2]
		while True:
			try:
				sleep(0.3)
				trade(token, user_id, session_id, trader_info, item)
				break
			except:
				continue
			else:
				break