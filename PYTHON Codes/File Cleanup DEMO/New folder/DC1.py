from glob import glob as fetch_files
from os import getcwd as pwd
from os import mkdir as mkd
from os.path import join as join
from os.path import basename as bsnm
from shutil import move as mv

print('--> \'Skip\' for PWD\n--> \'..\' for Previous Dir\n--> \'\\\' for Root Dir')
full_path=input("Path from where to get the file data: ")

if full_path == '':
    print('You are in PWD:')
    full_path=pwd()
elif full_path == '..':
    temp_path=pwd().split('\\')
    str1=''
    for i in range(len(temp_path)-1):
        str1+=temp_path[i]+'\\'
    full_path=str1
    print('PWD:\n'+pwd()+'\nNow:')
elif full_path == '\\':
    print('PWD:\n'+pwd()+'\nNow:')
    full_path = pwd()[:3]

print(full_path)

for file_path in fetch_files(join(full_path, '*.txt')):
    file_name = file_path.split('\\')[-1]
    new_dir = file_name[:1]
    try:
        mkd(join(full_path, new_dir))
    except WindowsError:
        #print('Folder already exists!')
        pass
    mv(file_path, join(new_dir, bsnm(file_path)))
