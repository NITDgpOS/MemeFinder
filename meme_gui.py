import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import meme_gui_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Meme_Finder (root)
    meme_gui_support.init(root, top)
    root.mainloop()

w = None
def create_Meme_Finder(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Meme_Finder (w)
    meme_gui_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Meme_Finder():
    global w
    w.destroy()
    w = None

# Managing Meme List

class Meme_Finder:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("459x450+420+166")
        top.title("Meme Finder")

        # Meme Displaying Canvas
        self.Canvas1 = Canvas(top)
        self.Canvas1.place(relx=0.04, rely=0.13, relheight=0.74, relwidth=0.9)
        self.Canvas1.configure(background="white")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(relief=RIDGE)
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(width=414)


        # Intiate Search Engine Button
        self.go = Button(top)
        self.go.place(relx=0.81, rely=0.06, height=26, width=67)
        self.go.configure(activebackground="#d9d9d9")
        self.go.configure(text='''Go''')
        self.go.configure(command= lambda: meme_gui_support.go(self.Canvas1))


        # Search Query Entry
        self.searchQuery = Entry(top)
        self.searchQuery.place(relx=0.15, rely=0.06, relheight=0.04
                , relwidth=0.62)
        self.searchQuery.configure(background="white")
        self.searchQuery.configure(font="TkFixedFont")
        self.searchQuery.configure(width=286)

        # Label for Search
        self.TLabel1 = ttk.Label(top)
        self.TLabel1.place(relx=0.04, rely=0.07, height=16, width=44)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(relief=FLAT)
        self.TLabel1.configure(text='''Search''')

        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        # Progress bar for tracking the search process
        self.TProgressbar1 = ttk.Progressbar(top)
        self.TProgressbar1.place(relx=0.05, rely=0.9, relwidth=0.52
                , relheight=0.0, height=19)
        self.TProgressbar1.configure(length="240")

        # Swith to previous meme, (C-1)%N
        self.previmg = Button(top)
        self.previmg.place(relx=0.65, rely=0.89, height=26, width=66)
        self.previmg.configure(activebackground="#d9d9d9")
        self.previmg.configure(text='''Previous''')
        self.previmg.configure(width=66)
        self.previmg.configure(command= lambda: meme_gui_support.prev(self.Canvas1))

        # Swith to next meme, (C+1)%N
        self.nextimg = Button(top)
        self.nextimg.place(relx=0.81, rely=0.89, height=26, width=64)
        self.nextimg.configure(activebackground="#d9d9d9")
        self.nextimg.configure(text='''Next''')
        self.nextimg.configure(width=64)
        self.nextimg.configure(command= lambda: meme_gui_support.next(self.Canvas1))



if __name__ == '__main__':
    vp_start_gui()


