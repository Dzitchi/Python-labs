list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

num_of_players = len(list_players)
team1 = list_players[0: (num_of_players // 2)]
team2 = list_players[(num_of_players // 2):]
print(team1)
print(team2)
