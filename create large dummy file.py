f = open('massive_file.txt',"a")
for i in range(0,15):
    f.write('a'*1024*1024*512)
f.close()

