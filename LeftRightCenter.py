import random

players = []
player_money = {}
total_money_in_play = 0


def get_players():
    new_player_name = input("Enter your first player\n")
    players.append(new_player_name.upper())

    while new_player_name.upper() != 'DONE':
        new_player_name = input("Enter another player name or type 'done' to start the game.\n")
        if new_player_name.upper() != 'DONE':
            players.append(new_player_name.upper())
    initiate_money()


def initiate_money():
    for player in players:
        player_money[player] = 3


def get_roll():
    rand = random.randrange(start=1, stop=7)
    if rand == 1:
        return "L"
    if rand == 2:
        return "R"
    if rand == 3:
        return "C"
    return "DOT"


def get_total_money_in_play():
    total_money = 0
    for value in player_money.values():
        total_money += value
    return total_money


def find_winner():
    for player in player_money.keys():
        if player_money[player] == 1:
            return player


def pass_money_left(player):
    player_index = players.index(player)
    if player_index != 0:
        passing_index = player_index - 1
    else:
        passing_index = len(players) - 1
    player_to_pass_to = players[passing_index]

    current_player_money = player_money[player]
    player_money[player] = current_player_money - 1
    player_money[player_to_pass_to] = player_money[player_to_pass_to] + 1
    print("{0}(${1}) just passed a dollar left to {2}(${3})\n".format(player, player_money[player],player_to_pass_to, player_money[player_to_pass_to]))


def pass_money_right(player):
    player_index = players.index(player)
    if player_index != len(players) - 1:
        passing_index = player_index + 1
    else:
        passing_index = 0
    player_to_pass_to = players[passing_index]

    current_player_money = player_money[player]
    player_money[player] = current_player_money - 1
    player_money[player_to_pass_to] = player_money[player_to_pass_to] + 1
    print("{0}(${1}) just passed a dollar right to {2}(${3})\n".format(player, player_money[player],player_to_pass_to, player_money[player_to_pass_to]))


def pass_money_center(player):
    current_player_money = player_money[player]
    player_money[player] = current_player_money - 1
    total_money_in_play = get_total_money_in_play()
    if total_money_in_play > 1:
        print("{0}(${1}) passed a dollar into the center. There are now ${2} in play.\n".format(player, player_money[player], total_money_in_play))
    else:
        winner = find_winner()
        print("{0} won!".format(winner))
        exit(0)


get_players()
total_money_in_play = get_total_money_in_play()

while total_money_in_play > 1:
    for player in players:
        current_player_money = player_money[player]
        if current_player_money > 0:
            for i in range(current_player_money):
                roll = get_roll()
                if roll == "L":
                    pass_money_left(player)
                if roll == "R":
                    pass_money_right(player)
                if roll == "C":
                    pass_money_center(player)
        else:
            print("Skipping {0} because they're out of money.".format(player))

print(player_money)




