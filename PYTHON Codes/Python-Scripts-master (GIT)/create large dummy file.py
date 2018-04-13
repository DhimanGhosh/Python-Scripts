f = open('Massive File.exe',"a")
for i in range(0,15):
    f.write('a'*1024*1024*400) #Just change the last value [1 = 15MB]
f.close()

