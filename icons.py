from json import load, dump
import configs
import requests

def get_icons():
    with open("icons.json", "r") as f:
        icons = load(f)
        f.close()
    return icons


def actualize_icons():
    icons = get_icons()
    url = f"https://discord.com/api/v8/users/"
    headers = {"Authorization": f"Bot {configs.TOKEN}"}

    ka = "502687173099913216"
    dudu = "536242240440369163"
    lanna = "744400468712882216"
    gibs = "417798802716622858"
    sayu = "686605969853251596"

    req = requests.get(url+ka, headers=headers).json()
    icons["ka"] = f"https://cdn.discordapp.com/avatars/{ka}/{req['avatar']}?size=2048"

    req = requests.get(url+dudu, headers=headers).json()
    icons["dudu"] = f"https://cdn.discordapp.com/avatars/{dudu}/{req['avatar']}?size=2048"

    req = requests.get(url+lanna, headers=headers).json()
    icons["lanna"] = f"https://cdn.discordapp.com/avatars/{lanna}/{req['avatar']}?size=2048"

    req = requests.get(url+gibs, headers=headers).json()
    icons["gibs"] = f"https://cdn.discordapp.com/avatars/{gibs}/{req['avatar']}?size=2048"

    req = requests.get(url+sayu, headers=headers).json()
    icons["sayu"] = f"https://cdn.discordapp.com/avatars/{sayu}/{req['avatar']}?size=2048"

    with open("icons.json", "w") as f:
        dump(icons, f, indent=4)
        f.close()