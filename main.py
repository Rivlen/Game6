from random import randint


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


def game_2001():
    players = {"pc": 0, "npc": 0}
    # turn1
    for player in players:
        players[player] += sum([randint(1, 6) for _ in range(2)])
    print(f"Your points: {players['pc']} \nComputer points: {players['npc']}")
    # after turn1
    while players['pc'] < 2001 and players['npc'] < 2001:
        input("Press Enter to continue...")
        for player in players:
            # check if player
            if player == "pc":
                # rolling the dice
                roll1 = randint(1, pick_dice())
                roll2 = randint(1, pick_dice())
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

        print(f"Your points: {players['pc']} \nComputer points: {players['npc']}")


if __name__ == '__main__':
    game_2001()
