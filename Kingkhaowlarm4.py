import os
os.system('cls')


players = [] # dict1, dict2, dict3, dict4, dict5
terminated_players = []
current_players = []
score_reducer = 1

for i in range(5):
    players.append(
        dict(
            id = i + 1,
            score = 0
        )
    )

playing_round = 0

while True:

    playing_round += 1

    print("Round", playing_round)

    while True:

        my_list = []
        duplicates = []

        for i in range(len(players)):
            print("Player" , players[i]['id'])
            my_list.append(int(input('your number: ')))
            if my_list[i] >=0 and my_list[i] <=100:
                    pass
            else:
                raise Exception("Please choose your number between 0-100")
            print("---------------------------------")


        for value in my_list:
            if my_list.count(value) > 1:
                if value not in duplicates:
                    duplicates.append(value)

        if len(duplicates) == 0:
            break
        else:
            os.system('cls')
            print (my_list)
            print("There are players with duplicate values.", duplicates, "This game void!!\nPlease choose your new number.")

    print(my_list)
                        
    average = sum(my_list)/len(my_list)
    game = average * 0.8

    for i in range(len(players)):
        my_list[i] = abs(game - my_list[i])

    # print("Calculated range:", my_list)

    min_value = min(my_list)
    winner = players[my_list.index(min_value)]['id']

    print("Average :",average,"\nGame :(Average * 0.8) = ",game)
    print("Winner is Player",winner)

    for player in players:
        if player['id'] == winner:
            continue
        player['score'] -= score_reducer

    for player in players:
        if player['score'] <= -10:
            print("Player %d was terminated (Score less than -10)" % (player['id']))
            terminated_players.append(player)

    current_players = players
    players = [player for player in current_players if player not in terminated_players] #? list comprehension

    # Ternary Operator ? :
    # players.length == 5 ? 1 : 2 # Conditional Expression
    score_reducer = 1 if len(players) == 5 else 2 # score_reducer = players.length == 5 ? 1 : 2

    print("---------------------------------")
    for i in range(len(players)):
        print("Score Player %d : %d" % (players[i]['id'], players[i]['score']))
    print("---------------------------------")

    if len(players) == 1:
        break

print("Player", players[0]['id'], "winner winner chicken dinner")
