from requests import post, get
from json import loads
from datetime import datetime

def send_message(channel_id, token, command):
    while True:
        request = post(f"https://discord.com/api/v10/channels/{channel_id}/messages?limit=1", headers={"authorization": token}, json={"content": command})
        if request.status_code in [200, 204]:
            return True
        else:
            return False

def retreive_message(channel_id, token, user_id):
    time = datetime.strptime(datetime.now().strftime("%x-%X"), "%x-%X")

    while (datetime.strptime(datetime.now().strftime("%x-%X"), "%x-%X") - time).total_seconds() < 5:
        request = get(f"https://discord.com/api/v10/channels/{channel_id}/messages", headers={"authorization": token})
        if request.status_code != 200:
            continue
        
        latest_message = loads(request.text)[0]
        
        if latest_message["author"]["id"] != "270904126974590976":
            continue
        
        if "referenced_message" in latest_message.keys():
            if latest_message["referenced_message"]["author"]["id"] == user_id:
                break

        else:
            break

    return latest_message