import random
teams = ["germany", "france", "england","canada","usa","argentina"]
random.shuffle(teams)
counter = int(len(teams)/2)
for item in range(1,counter+1):
    print(teams[item-1],"  VS  ", teams[item+2])

# 0 1 2 3 4 5 
# 0  2
# 1  4
# 3   5
    
        


