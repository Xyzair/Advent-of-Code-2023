day  = open("Data/Day1Input.txt", "r") 

tdata = day.read().split("\n")

numberStr = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numberNum = ["o1e", "t2o", "t3ree", "f4ur", "f5ve", "s6x", "se7en", "ei8ht", "n9ne"]


print(tdata)
data = [len(tdata)]
for x, value in enumerate(tdata):
    print(value, tdata[x])
    for i, val in enumerate(numberStr):
        value = value.replace(numberStr[i], numberNum[i])
    tdata[x] = value
    print(value)
print(tdata)

sum = 0
for val in tdata:
    
    first = ''
    last = ''
    count = 0
    for value in val:
        if value in ('0123456789'):
            # print(value)
            count +=1
            if count == 1:
                first = value
            last = value
    sum += int(first+last)
print(sum)

        