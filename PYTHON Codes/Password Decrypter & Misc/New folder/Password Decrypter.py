'''Directory Creator with file name, move each files to directory'''
import glob, os, shutil

dir_path=input("Path from where to get the file data ['this' for current]: ")
if dir_path[-1]=='/' or dir_path.split('/')[0] == 'this':
    path1=dir_path.split('/')
    path=''
    for i in range(1,len(path1)):
        path+='\\'+path1[i]
    dir_path=os.getcwd()+path+'\\'

'''Password Decrypter'''
fob=open(dir_path+'Password_Encrypted.txt','r')
string1=fob.readlines()
fob.close()
string=''.join(x for x in string1)
new_file_path=string.split('/')[0]
print(new_file_path)
folder=new_file_path.split('/')[0]
print(dir_path+folder)
try:
    #os.mkdir(os.path.join(dir_path, folder))
    os.makedirs(folder)
except WindowsError:
    # Handle the case where the target dir already exist.
    pass

'''
for file_path in glob.glob(os.path.join(folder, '*.*')):
    new_dir = file_path.rsplit('.', 1)[0]
    try:
        os.mkdir(os.path.join(folder, new_dir))
    except WindowsError:
        # Handle the case where the target dir already exist.
        pass
    shutil.move(file_path, os.path.join(new_dir, os.path.basename(file_path)))
'''


'''
fob=open('Password.txt','w')
for s in str_list:
    if s.split('HEL')[0] != 'P':
        fob.write(s.split('HEL')[1].split('PK')[0])
fob.close()'''
