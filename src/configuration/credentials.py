from json import load,loads
from requests import get
from discord.gateway import gateway 

def load_credentials(token):
    request = get("https://discord.com/api/v10/users/@me", headers={"authorization": token})
    request = loads(request.text)
    data = [request["id"], gateway(token)]
    return data

def load_trader(trader_token):
    request = get("https://discord.com/api/v10/users/@me", headers={"authorization": trader_token})
    request = loads(request.text)
    data = [request["id"], gateway(trader_token), trader_token]
    return data