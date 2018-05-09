from time import gmtime, strftime, sleep, time

arr = list(input('Any Integer Number: '))
print(arr)

for _ in range(10):
    current_mil_sec = int(round(time() * 1000))
    current_sec = int(strftime('%S', gmtime()))
    arr = [int(a) for a in arr]
    #r = int(input('Rotation Value: ')) % len(arr)
    r = ((current_sec % 10) * (current_mil_sec % 10))%10
    print(str(arr[r:]+arr[:r])+': Rotation Value = '+str(r))
    sleep(1)
