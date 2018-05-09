from time import gmtime, strftime, time

for _ in range(10):
    current_mil_sec = int(round(time() * 1000))
    current_sec = int(strftime('%S', gmtime()))
    r = (current_sec % 100) * (current_mil_sec % 1000)
    print('Generated Random Number: '+str(r))
