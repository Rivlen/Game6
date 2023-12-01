from random import randint
from flask import Flask, request, render_template

app = Flask(__name__)


def pick_dice():
    while True:
        try:
            pick = int(input("Pick from D3, D4, D6, D8, D10, D12, D20, D100: ")[1:])
        except ValueError:
            print("Invalid input")
            continue
        dice_choice = [3, 4, 6, 8, 10, 12, 20, 100]
        if pick not in dice_choice:
            print("Invalid choice")
            continue
        return pick


@app.route('/', methods=["GET", "POST"])
def game_2001():
    global players

    if request.method == "GET":
        for player in players:
            players[player] = sum([randint(1, 6) for _ in range(2)])
        return render_template("main_page.html", pc=players["pc"], npc=players["npc"])

    elif request.method == "POST":
        for player in players:
            # check if player
            if player == "pc":
                # rolling the dice
                pick1 = int(request.form.get("number1"))
                pick2 = int(request.form.get("number2"))
                roll1 = randint(1, pick1)
                roll2 = randint(1, pick2)
                roll = roll1 + roll2
                # checking and adding
                if roll == 7:
                    players[player] += 7
                    players[player] = int(players[player] / 7)

                elif roll == 11:
                    players[player] += 11
                    players[player] *= 11

                else:
                    players[player] += roll
            elif player == "npc":
                # rolling the dice
                roll = sum([randint(1, 6) for _ in range(2)])
                # checking and adding
                if roll == 7:
                    players[player] += 7
                    players[player] = int(players[player] / 7)

                elif roll == 11:
                    players[player] += 11
                    players[player] *= 11

                else:
                    players[player] += roll
        return render_template("main_page.html", pc=players["pc"], npc=players["npc"])


if __name__ == '__main__':
    players = {"pc": 0, "npc": 0}
    app.run(debug=True)
