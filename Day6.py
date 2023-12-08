day  = open("Data/Day6Input.txt", "r") 

tdata = day.read().split("\n")

print(tdata)
time =[]
distance =[]

val = tdata[0]
for value in val.split(" ")[1:]:
    if value is not '':
        time.append(int(value))

val = tdata[1]
for value in val.split(" ")[1:]:
    if value is not '':
        distance.append(int(value))

print(time, distance)

print("Data Loaded")

total = 1
for i,t in enumerate(time):
    d = distance[i]
    sum = 0
    # test all possible times and count the valid ones.
    for tea in range(t):
        if tea * (t - tea) > d:
            sum += 1
    total *= sum

print("Part 1:", total)
print("Part 2 was done by removing the white spaces between numbers")
             


