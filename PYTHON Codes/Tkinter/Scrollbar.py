#PROBLEM

# Create root
self.root = Tk()
self.root.geometry('1000x500+0+0')

# Create canvas
self.canvas = Canvas(self.root)
self.canvas.pack(side=TOP, fill=BOTH, expand=TRUE)

# Create scrollbars
self.xscrollbar = Scrollbar(self.root, orient=HORIZONTAL, command=self.canvas.xview)
self.xscrollbar.pack(side=BOTTOM, fill=X)
self.yscrollbar = Scrollbar(self.root, orient=VERTICAL, command=self.canvas.yview)
self.yscrollbar.pack(side=RIGHT, fill=Y)

# Attach canvas to scrollbars
self.canvas.configure(xscrollcommand=self.xscrollbar.set)
self.canvas.configure(yscrollcommand=self.yscrollbar.set)

# Create frame inside canvas
self.frame = Frame(self.canvas)
self.canvas.create_window((0,0), window=self.frame, anchor=NW)
self.frame.bind('<Configure>', self.set_scrollregion)

# Write db contents to canvas
self.print_dbcontents()

# Invoke main loop
self.root.mainloop()

def set_scrollregion(self, event):
    self.canvas.configure(scrollregion=self.canvas.bbox('all'))

#In this implementation, I can only get scrolling to work in one direction, depending on how I pack the canvas

self.canvas.pack(side=TOP, fill=BOTH, expand=TRUE) # scrolling works in x but not y
self.canvas.pack(side=LEFT, fill=BOTH, expand=TRUE) # scrolling works in y but not x

#I just need to get horizontal and vertical scrolling to work simultaneously, or find an alternate solution.







#SOLUTION
'''
I don't see any code that would prevent the scrollbars from working. I do see a problem that prevents one of the scrollbars from showing up where you expect it (assuming you expect them to appear in the traditional place). Is that what you mean whey you say you want them to "work simultaneously"?

Your layout is done with the following code and in the following order:
'''
self.canvas.pack(side=TOP, fill=BOTH, expand=TRUE)
self.xscrollbar.pack(side=BOTTOM, fill=X)
self.yscrollbar.pack(side=RIGHT, fill=Y)
'''
That first line causes the canvas to fill the whole top of the widget, all the way from the left to all the way to the right. When you later place the yscrollbar on the right, this means it goes to the right of the space left over after the canvas fills up the top. Since the canvas fills the top, there is no left over space to the right, only below. Thus, your scrollbar will appear as a tiny widget about the height of the horizontal scrollbar below the canvas.

A quick fix is to pack the vertical scrollbar first, then the horizontal, and then the canvas. Your "major" widget should always be one of the last things you pack/grid. One, you do that for the obvious reason that you need to in this case to get the desired effect, but also because it makes your resize behavior right. I'm getting off topic to explain why in this answer, so read this answer on stackoverflow for more information.

Second, when working with scrollbars it's best to use grid if you want a professional appearance. If you use pack, the scrollbars will not align property in the corner in which they meet. You want them to look like this, with a small blank space in the lower-right corner:

  ||
==
However, if you use pack they'll look like one of these:

   ||    -or-      ||
 ====            ==||
Finally, I encourage you to not import *, it could cause problems down the road. Instead, get in the habit of doing import Tkinter as tk and then prefixing all of the tk commands with "tk." (eg: tk.Canvas, etc). You'll see why this matters the first time you try to mix ttk and tkinter widgets in the same UI, but you could have problems elsewhere if you also "import *" from other packages as well. Plus, this way it's obvious when you're using tk features and when you're using features from other packages.
'''