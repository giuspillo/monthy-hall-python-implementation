
import random 

tot = 0
wins = 0
reps = 100000

for i in range(0, reps):

    # 3 doors: false=goat, true=car
    doors = [False, False, False]
    car = random.randint(0,2)
    doors[car] = True
    
    # goat indices
    goats = [i for i, g in enumerate(doors) if g == False]
    # print('doors:', doors)
    
    # user choice
    choice = random.randint(0,2)
    # print('user choice:', choice)

    # choose a door with a goat to be opened
    # if the user choose a goat, open the other door
    # otherwise, open randomly one of the two doors
    if doors[choice] == True:
        opened = goats[random.randint(0,1)]
    else:
        opened = list(set([0, 1, 2]) - set([choice, car]))[0]
    # print('open the door', opened)
    
    # find the remaining door (not chosen and not opened)
    change = list(set([0, 1, 2]) - set([choice, opened]))[0]
    # print('user changes on door', change)
    
    if change == car:
        wins += 1
    tot += 1
    

prob = (float) (wins / tot)
print(wins, 'wins over', tot, 'total: ', prob)





