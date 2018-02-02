import glob,os

path=input("Path from where to get the file data ['this' for CWD]: ")
if path=='this':
    path=os.getcwd()
    print('You are in {}\n'.format(path))
elif path==os.getcwd() or path[0:-1]==os.getcwd():
    print("You are in Current Working Directory[CWD]!\n")
#print('You are in {}!'.format(path.rsplit('\\',1)[1]))

files_list_with_path=glob.glob('{}\*.*'.format(path))
files_list=[] #Just for printing

#Extracting only the file name from the path in the list, to a new list
for file in files_list_with_path:
    files_list.append(file.split('\\')[-1])

#Looking for only textual files, eliminating others [NOT_WORKING]
'''
ext_list=['exe','lnk','ini','pptx']

# for i in range(len(ext_list)):
#     count=len(files_list)-1
#     while count>0:
#         if ext_list[i]==files_list[count].split('.')[-1]:
#             files_list.remove(files_list[count])
#             #files_list.replace(files_list[count],'')
#         count-=1


# for file_pos in range(0,len(files_list)-1):
#     if files_list[file_pos].split('.')[-1] in ext_list:
#         files_list.pop(file_pos)
'''

#Prints the files present, in a .txt file
'''
files_present='\n'.join(x for x in files_list)
fob=open('{}\Files Present.txt'.format(path),'a')
fob.write(files_present)
fob.close()
'''

#Prints the files present, in console, for options
i=1
for file in files_list:
    print('{}. {}'.format(i,file))
    i+=1

#Prints the contents of a particular file, in a .txt file, in that location of the file
'''
i=1
for file in files_list:
    print('{}. {}'.format(i,file))
    i+=1
try:
    ch=int(input('\nWhich file to open: '))
    fob=open(files_list_with_path[ch-1],'r')
    file_contents=fob.readlines()
    fob.close()
    fob=open('{}\{} contents.txt'.format(path,files_list[ch-1]),'a')
    file_content=''.join(x for x in file_contents)
    fob.write(file_content)
    fob.close()
    print('File Created!')
except:
    print('Please enter numbers from 1-{}'.format(i-1))
'''


#Prints the contents of a particular file, in console
try:
    ch=int(input('\nWhich file to open: '))
    fob=open(files_list_with_path[ch-1],'r')
    file_contents=fob.readlines()
    fob.close()
    file_content=''.join(x for x in file_contents)
    print(file_content)
except:
    print('Please enter numbers from 1-{}'.format(i-1))

