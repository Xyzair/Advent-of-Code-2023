from collections import Counter

day  = open("Data/Day7Input.txt", "r") 

tdata = day.read().split("\n")

data =[]

replacer = {"A":"M", "K":"L", "Q":"K", "J":"J", "T":"I", "9":"H", "8":"G", "7":"F", "6":"E", "5":"D", "4":"C", "3":"B", "2":"A"}

for val in tdata:
    v = val.split(" ")
    updated_string =""
    for string in v[0]:
        updated_string += replacer[string]
    data.append((Counter(updated_string), int(v[1]), updated_string, v[0]))
print("DATA", data[0][0][0])

stringdata = []

for i, hand in enumerate(data):
    print("V:", hand)
    string = ''
    temp = []
    for val in hand[0]:
        temp.append(hand[0][val])
    temp.sort(reverse=True)
    
    for val in temp:
        string += str(val)
    # print(string)
    stringdata.append((string, data[i][1], data[i][2], data[i][3]))


sorter = lambda x: (x[0], x[2])

sorted = sorted(stringdata, key = sorter )
# print(stringdata)
# print(sorted)

Total = 0
for i, val in enumerate(sorted):
    Total += (i+1) * val[1]
    # print(Total)

print(Total)
