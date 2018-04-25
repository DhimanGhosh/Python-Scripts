import glob, os, shutil

folder=input("Path from where to get the file data [Skip for current]: ")
if folder == '':
    folder = os.getcwd()
elif folder[0] == '\\':
    folder = os.getcwd() + folder
print(folder)

for file_path in glob.glob(os.path.join(folder, '*.jpg')):
    print(file_path)
    file_name_ext = file_path.split('\\')[-1]
    file_name = file_name_ext.split('.')[0]
    new_dir = file_name[:21]
    
    try:
        os.mkdir(os.path.join(folder, new_dir))
    except WindowsError:
        # Handle the case where the target dir already exist.
        pass
    shutil.move(file_path, os.path.join(new_dir, os.path.basename(file_path)))
