day  = open("Data/Day5Input.txt", "r") 

tdata = day.read().split("\n\n")
data = []
# Start range, end range, Range Length
# print(tdata)

# print(tdata)
seed = tdata[0].split()[1:]

# print("Seed",seed)
for i, val in enumerate(seed):
     seed[i] = int(val)

print("Start Seed:", seed)


# Current is the current data to be processed into a dictionary
def make_map(current):
    thisdict = []
    print("CURRENT", current)

    for val in current:
        temp = val.split(' ')
        start = int(temp[0])
        end = int(temp[1])
        length = int(temp[2])

        thisdict.append([start,end,length])
        print("thisdict",thisdict)

    return thisdict


# update seed through the current table
def seed_update(seed, thisdict):
    for i,value in enumerate(seed):
        print("AAAA",value, thisdict)
        for x,val in enumerate(thisdict):
            if 0 < value - thisdict[x][1] < thisdict[x][2]:
                seed[i] = value - thisdict[x][1] + thisdict[x][0]
    print("SEED", seed)
    return seed

tdata = tdata[1:]
current =tdata[0].split("\n")[1:]


print(seed)
for value in tdata:
    current = value.split("\n")[1:]
    seed = seed_update(seed, make_map(current))
   
print("Lowest Seed", min(seed))

