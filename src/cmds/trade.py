from discord.message import send_message, retreive_message
from discord.button import interact_button
from time import sleep

def trade(channel_id, token, user_id, session_id, trader_info, item):
    send_message(channel_id, token, f"pls shop {item}")

    latest_message = retreive_message(channel_id, token, user_id)

    total = latest_message["embeds"][0]["title"].split("(")[1][:-7]

    send_message(channel_id, token, f"pls trade {int(total)} {item} {trader_info[0]}")

    latest_message = retreive_message(channel_id, token, user_id)

    if latest_message is None:
        return

    interact_button(channel_id, token, latest_message["components"][0]["components"][-1]["custom_id"], latest_message, session_id)

    sleep(1)

    latest_message = retreive_message(channel_id, trader_info[2], trader_info[0])

    if latest_message is None:
        return

    interact_button(channel_id, trader_info[2], latest_message["components"][0]["components"][-1]["custom_id"], latest_message, trader_info[1])