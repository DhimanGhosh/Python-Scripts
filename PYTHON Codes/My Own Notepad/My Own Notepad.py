from tkinter import *
from tkinter import filedialog

filename = None

def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)

def saveFile():
    global filename
    t = text.get(0.0, END)
    f = open(filename, 'w')
    f.write(t)
    f.close()

def saveAs():
    f = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        showerror(title='Oops!', message='Unable to save file...')

def openFile():
    f = filedialog.askopenfile(mode='r')
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)

def updateService():
    root1 = Tk()
    root1.title("Custom Text Editor")
    root1.minsize(width=350, height=150)
    root1.maxsize(width=350, height=150)

    t='Current Version: v0.1\n\n\n\nChecking for updates...'
    
    
    text1 = Text(root1, state='normal', width=350, height=150)
    text1.insert(0.0, t)
    text1.configure(state='disabled')
    text1.pack()

    root1.mainloop()

def aboutDialog():
    root1 = Tk()
    root1.title("About Us")
    root1.minsize(width=350, height=150)
    root1.maxsize(width=350, height=150)

    t='Custom Text Editor\n\n\n\n\tCreated by Dhiman Ghosh @2018'
    
    text1 = Text(root1, state='normal', width=350, height=150)
    text1.insert(0.0, t)
    text1.configure(state='disabled')
    text1.pack()

    root1.mainloop()

root = Tk()
root.title("Custom Text Editor")
root.wm_iconbitmap('favicon.ico')
window_width=800
window_height=400
root.minsize(width=window_width, height=window_height)
root.maxsize(width=window_width, height=window_height)
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

text = Text(root, width=window_width, height=window_height)
text.configure(yscrollcommand=scrollbar.set)
text.pack()
scrollbar.config(command=text.yview) #To give Bar control

#root.bind_all('<Control-Key-O>',openFile)

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label='New', command=newFile, accelerator='Ctrl + N')
filemenu.add_command(label='Open', command=openFile, accelerator='Ctrl + O')
filemenu.add_command(label='Save', command=saveFile, accelerator='Ctrl + S')
filemenu.add_command(label='Save As...', command=saveAs)
filemenu.add_separator()
filemenu.add_command(label='Quit', command=root.quit, accelerator='Ctrl + Q')
menubar.add_cascade(label='File', menu=filemenu)

helpmenu = Menu(menubar)
helpmenu.add_command(label='Check For Updates...', command=updateService)
helpmenu.add_separator()
helpmenu.add_command(label='About Us', command=aboutDialog)
menubar.add_cascade(label='Help', menu=helpmenu)

root.config(menu=menubar)
root.mainloop()
