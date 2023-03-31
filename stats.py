import json
from datetime import timedelta
from cookie_clicker import CookieClicker

def update_stats(cc:CookieClicker):
    with open("stats.json","r") as file:
        data = json.load(file)
    
    data["time"]+=int(cc.time)
    data["clicks"]+=cc.count
    
    with open("stats.json","w") as file:
        json.dump(data,file,indent=4)

def show_stats():
    with open("stats.json","r") as file:
        data = json.load(file)
        print(f"Statistics since the beginning (number of clicks and execution-time):")
        print(f"\t- {data['clicks']} clicks")
        print(f"\t- {timedelta(seconds = data['time'])}")

def show_cc_stats(cc:CookieClicker):
    print("Game statistics:")
    print(f"\t- {cc.count} clicks")
    print(f"\t- {int(cc.time)}s")
    print(f"\t- {cc.frequency():.0f}Hz")