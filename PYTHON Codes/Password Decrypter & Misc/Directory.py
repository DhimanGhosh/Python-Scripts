import os,glob

c=0
#while glob.glob(os.getcwd())!=None:
def crt():
    if c==5:
        exit()
    else:
        c+=1
        try:
            os.makedirs("Test")
            os.chdir("Test/")
            f=open('{}.txt'.format(c))
            f.close()
            crt()
        except WindowsError:
            # Handle the case where the target dir already exist.
            pass
'''
while True:
    try:
        os.removedirs("Test")
        os.chdir("..")
    except WindowsError:
        # Handle the case where the target dir already exist.
        pass
'''
