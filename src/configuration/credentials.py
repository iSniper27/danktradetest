from json import load,loads
from requests import get
from discord.gateway import gateway 

def load_credentials(cwd):
    credentials = load(open(f"{cwd}credentials.json", "r"))
    data = []
    for index in range(len(credentials["tokens"])):
        request = get("https://discord.com/api/v10/users/@me", headers={"authorization": credentials["tokens"][index]})
        request = loads(request.text)
        data.append([request["id"], gateway(credentials["tokens"][index]), credentials["tokens"][index]])
    return data

def load_trader(cwd):
    credentials = load(open(f"{cwd}credentials.json", "r"))
    token = credentials["tradertoken"]
    request = get("https://discord.com/api/v10/users/@me", headers={"authorization": token})
    request = loads(request.text)
    data = [request["id"], gateway(token), token, credentials["tradechannel_id"]]
    return data