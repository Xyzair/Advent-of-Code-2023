day  = open("Data/Day3Input.txt", "r") 

tdata = day.read().split("\n")
data = []

for y, value in enumerate(tdata):
    temp = []
    for x, val in enumerate(value):
        temp.append(val)
    data.append(temp)

print("Data Loaded Successfully")
# for val in data:
#     print(val)


added = []
def acquire_number(arr, x, y):
    if ((x,y) in added) or arr[y][x].isdigit() == False:
            return 0
    
    # Find left most digit
    left = False
    while left == False:
        if(arr[y][x].isdigit()):
            # print("here", x,y, arr[y][x])
            added.append((x,y))
            if( x-1 >= 0 and arr[y][x-1].isdigit()):
                x-=1
            else:
                left = True

        else:
            left = True
            x+=1
    

    # Acquire number
    number = ''
    end = False
    while end == False:
        # print("???",x,y)
        if(arr[y][x].isdigit()):
            number += arr[y][x]
            if (x,y) not in added:
                added.append((x,y))
            
            if( x+1 < len(arr[0])):
                x+=1
            else:
                end = True
        else:
            end = True

    if number.isdigit():
        print("To be Added: ",number)
        return int(number)
    else:
         return 0
                  
# print("returned: ", acquire_number(data, 5, 0))
# print("returned: ", acquire_number(data, 6, 0))


sum = 0
for y1, value in enumerate(data):
    for x1, val in enumerate(value):
        if data[y1][x1] not in ('.0123456789'):
            print("Symbol:", data[y1][x1], "Location:", x1,y1)
            for y in range(3):
                for x in  range(3):
                    tx = x - 1 + x1
                    ty = y - 1 + y1
                    # print(tx, ty)
                    # make sure we're in bounds
                    if (tx < 0 or ty < 0) or tx >= len(data[0]) or ty >= len(data):
                        print("breaking:", tx, ty, len(data[0]), ty >= len(data))
                        break

                    
                    sum += acquire_number(data, tx, ty)
            print("running Total: ", sum)
            
print("Total:", sum)