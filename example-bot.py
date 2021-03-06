#!/usr/bin/env python3

import os, time, random, requests

lastMove = "up"
opposites = {"left":"right", "right":"left", "up":"down", "down":"up"}
while True:
    try:
        x = int(requests.get(
            "https://raw.githubusercontent.com/programical/gitland/master/players/programical/x",
            headers={"Cache-Control": "no-cache", "Pragma": "no-cache"}
        ).text)

        y = int(requests.get(
            "https://raw.githubusercontent.com/programical/gitland/master/players/programical/y",
            headers={"Cache-Control": "no-cache", "Pragma": "no-cache"}
        ).text)
    except Exception as err:
        print(str(err))
        continue

    if x < 5:
        move = "right"
    elif x > 17:
        move = "left"
    elif y < 5:
        move = "down"
    elif y > 17:
        move = "up"
    else:
        allowedMoves = "right left up down".replace(opposites[lastMove], "").replace("  ", " ").strip()
        print("since the last move was " + lastMove + ", picking from " + allowedMoves)
        move = random.choice(allowedMoves.split(" "))

    open("act", "w").write(move)
    os.system("git add -A")
    os.system("git commit -m \"move " + open("act").read().strip() + "\"")
    os.system("git push origin master")

    lastMove = move
    time.sleep(61)
