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
from cmds.trade import trade_item, trade_wallet

credentials = load_credentials(cwd)

while True:
	print("command list:\n1)trade item\n2)trade wallet\n")
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
					trade_item(token, user_id, session_id, trader_info, item)
					break
				except:
					continue
	
	if command == 2:
		trader_info = load_trader(cwd)

		for index in range(len(credentials)):
			user_id = credentials[index][0]
			session_id = credentials[index][1]
			token = credentials[index][2]
			while True:
				try:
					sleep(0.3)
					trade_wallet(token, user_id, session_id, trader_info)
					break
				except Exception as e:
					print(e)
					continue