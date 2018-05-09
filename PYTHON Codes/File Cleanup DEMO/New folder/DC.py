import glob, os, shutil

path=input("Path from where to get the file data [Skip for PWD]: ")
if path == '':
    path=os.getcwd()

for file_path in glob.glob(os.path.join(path, '*.*')):
    file_name = file_path.split('\\')[-1]
    new_dir = file_name[:21]
    try:
        os.mkdir(os.path.join(path, new_dir))
    except WindowsError:
        print('Folder already exists!')
        pass
    shutil.move(file_path, os.path.join(new_dir, os.path.basename(file_path)))
