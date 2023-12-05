day  = open("Data/Day1Input.txt", "r") 

tdata = day.read().split("\n")

print(tdata)

sum = 0
for val in tdata:
    first = ''
    last = ''
    count = 0
    for value in val:
        if value in ('0123456789'):
            print(value)
            count +=1
            if count == 1:
                first = value
            last = value
    sum += int(first+last)
print(sum)

        