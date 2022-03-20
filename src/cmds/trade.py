from discord.message import send_message, retreive_message
from discord.button import interact_button
from time import sleep

def trade_item(token, user_id, session_id, trader_info, item):
    channel_id = trader_info[3]

    send_message(channel_id, token, f"pls shop {item}")

    latest_message = retreive_message(channel_id, token, user_id)

    total = latest_message["embeds"][-1]["title"].split("(")[1][:-7]

    if int(total) == 0:
        return

    send_message(channel_id, token, f"pls trade {int(total)} {item} {trader_info[0]}")

    latest_message = retreive_message(channel_id, token, user_id)

    if latest_message is None:
        return

    interact_button(channel_id, token, latest_message["components"][-1]["components"][-1]["custom_id"], latest_message, session_id)

    sleep(0.3)

    latest_message = retreive_message(channel_id, trader_info[2], trader_info[0])

    if latest_message is None:
        return

    interact_button(channel_id, trader_info[2], latest_message["components"][0]["components"][-1]["custom_id"], latest_message, trader_info[1])

def trade_wallet(token, user_id, session_id, trader_info):
    channel_id = trader_info[3]

    send_message(channel_id, token, "pls bal")

    latest_message = retreive_message(channel_id, token, user_id)

    total = latest_message["embeds"][-1]["description"].split("\n")[0][14:].replace(",", "")

    send_message(channel_id, token, f"pls trade {int(total)*(1/1.03)} {trader_info[0]}")

    latest_message = retreive_message(channel_id, token, user_id)

    if latest_message is None:
        return

    interact_button(channel_id, token, latest_message["components"][-1]["components"][-1]["custom_id"], latest_message, session_id)

    sleep(0.3)

    latest_message = retreive_message(channel_id, trader_info[2], trader_info[0])

    if latest_message is None:
        return

    interact_button(channel_id, trader_info[2], latest_message["components"][0]["components"][-1]["custom_id"], latest_message, trader_info[1])