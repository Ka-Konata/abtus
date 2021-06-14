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

    # Declarando os ID's --------------------------------------------
    # Donos dos perfils
    ka = "502687173099913216"
    dudu = "536242240440369163"

    # Amigos: Ka
    lanna = "744400468712882216"
    gibs = "417798802716622858"
    sayu = "686605969853251596"
    lin = "479448688364617729"
    snay = "208969161282551810"
    kah = "695461545219588147"

    # Amigos: Dudu
    bruno = "708934788354015284"
    andri = "853299059858210858"

    # Pegando as URL's --------------------------------------------
    # Donos dos perfils
    req = requests.get(url+ka, headers=headers).json()
    icons["ka"] = f"https://cdn.discordapp.com/avatars/{ka}/{req['avatar']}?size=2048"

    req = requests.get(url+dudu, headers=headers).json()
    icons["dudu"] = f"https://cdn.discordapp.com/avatars/{dudu}/{req['avatar']}?size=2048"

    # Amigos: Ka
    req = requests.get(url+lanna, headers=headers).json()
    icons["lanna"] = f"https://cdn.discordapp.com/avatars/{lanna}/{req['avatar']}?size=2048"

    req = requests.get(url+gibs, headers=headers).json()
    icons["gibs"] = f"https://cdn.discordapp.com/avatars/{gibs}/{req['avatar']}?size=2048"

    req = requests.get(url+sayu, headers=headers).json()
    icons["sayu"] = f"https://cdn.discordapp.com/avatars/{sayu}/{req['avatar']}?size=2048"

    req = requests.get(url+lin, headers=headers).json()
    icons["lin"] = f"https://cdn.discordapp.com/avatars/{lin}/{req['avatar']}?size=2048"

    req = requests.get(url+snay, headers=headers).json()
    icons["snay"] = f"https://cdn.discordapp.com/avatars/{snay}/{req['avatar']}?size=2048"

    req = requests.get(url+kah, headers=headers).json()
    icons["kah"] = f"https://cdn.discordapp.com/avatars/{kah}/{req['avatar']}?size=2048"

    # Amigos: Dudu

    req = requests.get(url+bruno, headers=headers).json()
    icons["bruno"] = f"https://cdn.discordapp.com/avatars/{bruno}/{req['avatar']}?size=2048"

    req = requests.get(url+andri, headers=headers).json()
    icons["andri"] = f"https://cdn.discordapp.com/avatars/{andri}/{req['avatar']}?size=2048"

    with open("icons.json", "w") as f:
        dump(icons, f, indent=4)
        f.close()