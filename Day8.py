import re

day  = open("Data/Day8Input.txt", "r") 

t= day.read().split("\n\n")
key = t[0]
print(key, t)
tdata = t[1].split("\n")
# tdata = tdata[1:]
print(tdata)

path = {}
root = "AAA"
for val in tdata:
    path[val[0:3]] = val[7:10], val[12:15]

print(root, path)

print("Data Loaded")

current = root
step = 0
z_found = False


while z_found == False:
    k = key[step%len(key)]
    if k in "L":
        current = path[current][0]
    elif k in "R":
        current = path[current][1]
    else:
        print("FAILURE")
        z_found = True

    if current == "ZZZ":
        z_found = True
    step += 1
    if step%1000000 == 0:
        print(k, current, step)
    
print(step)
