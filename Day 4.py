day  = open("Data/Day4Input.txt", "r") 

tdata = day.read().split("\n")
data = []

print(tdata[0])
print("Data Loaded Successfully")

for i, val in enumerate(tdata):
    print(val)
    data.append(val.split(":")[1].split("|"))
    print(data[i])
    data[i] = set(data[i][0].split(" ")).intersection(set(data[i][1].split(" ")))



sum = 0
for val in data:
    print(val)
    print(len(val))
    if len(val) > 1:
        sum += 2 ** (len(val) - 2)

print(sum)
