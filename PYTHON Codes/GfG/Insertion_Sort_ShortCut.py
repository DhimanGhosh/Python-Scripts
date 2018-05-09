arr = []
while True:
    print("(-999 to end)",end=' ')
    num = int(input('Num: '))
    if len(arr)==0:
        arr.append(num)
    elif num==-999:
        break
    else:
        for i in range(len(arr)):
            if num <= arr[i]:
                arr.insert(i, num)
                break
            elif i == len(arr)-1:
                arr.append(num)
                break

print(arr)
