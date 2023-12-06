day  = open("Data/Day2Input.txt", "r") 

tdata = day.read().split("\n")
data = []

# print(tdata)

# put rounds into RGB and then append into rounds
for val in tdata:
    # print(val.split(": ")[1].split("; "))
    games = val.split(": ")[1].split("; ")
    rounds=[]
    for round in games:
        r = round.split(", ")
        # print(r)
        
        red = 0
        green = 0 
        blue = 0

        for numb in round.split(", "):
            if 'red' in numb:
                red = int(numb.split(" ")[0])
            elif 'green' in numb:
                green = int(numb.split(" ")[0])
            elif 'blue' in numb:
                blue = int(numb.split(" ")[0])
        rounds.append((red, green, blue))
    data.append(rounds)

# print(data)
print("Data import complete")

def round_compare(red, green, blue, game):
    valid = True
    
    for round in game:
    
        if round[0] > red:
            valid = False
    
        elif round[1] > green:
            valid = False
    
        elif round[2] > blue:
            valid = False
    
    return valid

sum = 0
for i, value in enumerate(data):
    if round_compare(12, 13, 14, value):
        sum += i + 1

print("Part 1 Total:", sum) 
        
print("Part 2 Start")

def minimum_power(game):
    # print("Game", game)
    red = 0
    green = 0 
    blue = 0
    
    for round in game:
        if round[0] > red:
            red = round[0]
    
        if round[1] > green:
            green = round[1]
    
        if round[2] > blue:
            blue = round[2]

    if red == 0:
        red = 1
    if blue == 0:
        blue = 1
    if green == 0:
        green = 1
    
    # print("Total:", red * green * blue)
    
    return red * green * blue

sum2 = 0
for val in data:
    sum2 += minimum_power(val)

print("Part 2 Total:", sum2)