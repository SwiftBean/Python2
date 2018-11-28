game_list = ("halo : reach",
             "skyrim",
             "uno",
             "cod:bo2",
             "halo 4",
             "diablo 3: ROS",
             "cards against humanity",
             "starcraft 2",
             "cod:mw3",
             "minecraft")
print(len(game_list))
num5game=game_list[4]
print(num5game)
middle5 = game_list[3:7]
print(middle5)
last4 = game_list[6:]
print(last4)
evens = game_list[::2]
print(evens)
backward = game_list[::-1]
for i in game_list:
    print(i)
print(game_list)
game_list +=("11",12,13.0,14,"15")
print(game_list)
