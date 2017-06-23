fob=open('Webdriver Help.txt','r')
string1=fob.readlines()
fob.close()
string=''.join(x for x in string1)
str_list=string.split('\', \'')
fob=open('Webdriver Help.txt','w')
for s in str_list:
    fob.write(s+'\n')
fob.close()
