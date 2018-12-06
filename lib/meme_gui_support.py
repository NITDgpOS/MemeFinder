#  ____   _____  _____  _____  _____  _____  _____  _____  _____  ____
# |    \ |   __||  _  || __  ||   __||     ||  _  ||_   _||   __||    \
# |  |  ||   __||   __||    -||   __||   --||     |  | |  |   __||  |  |
# |____/ |_____||__|   |__|__||_____||_____||__|__|  |_|  |_____||____/

import sys
import subprocess
from os import listdir
from os.path import isfile, join
import search


try:
    from Tkinter import *
    import ttk
    py3 = 0
except ImportError:
    from tkinter import *
    import tkinter.ttk as ttk
    py3 = 1

from PIL import Image, ImageTk


class memes:
    def __init__(self):
        self.memeList = ['nofile']
        self.currentImage = 0


m = memes()


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


def getMemeList(query):
    source = 'database/data2.txt'
    m.memeList = search.get_score(search.create_index(
        source), search.generate_query(query))


def display(canvas, image_path):
    x = Image.open(image_path)
    gif1 = ImageTk.PhotoImage(image=x.resize((300, 300), Image.ANTIALIAS))
    canvas.create_image(200, 150, image=gif1)
    canvas.gif1 = gif1


def settings_collect():

    # Collecting Subreddits
    root = Tk()
    root.title("Settings:User Input")
    root.geometry("300x100+420+166")
    label = Label(root, text="Enter the subreddits, separated by commas")
    label.pack(side=TOP)
    e = Entry(root)
    e.place(relx=0.15, rely=0.20, relheight=0.30, relwidth=0.65)

    def callback():
        msg = e.get().split(',')
        temp1 = open('./temp.sh', 'wb')
        with open('./collect.sh', 'r') as f:
            for line in f:
                if line.startswith("python .."):
                    line = line.strip()
                    for i in range(0, len(msg)):
                        line = line + " " + msg[i]
                    line = line + "\n"
                temp1.write(bytes(line))
        #temp1.write(bytes("\n chmod a+x temp.sh", "utf-8"))
        temp1.close()
        #shutil.move("./temp1.txt", "./temp.sh")
        subprocess.call("chmod a+x temp.sh", shell=True)
        # Calling the collect bash script
        subprocess.call("./temp.sh", shell=True)
        root.destroy()

    def callbackerr():
        root.destroy()
    b = Button(root, text="COLLECT", command=callback)
    b.place(relx=0.05, rely=0.7, height=26, width=67)
    c = Button(root, text="CLOSE", command=callbackerr)
    c.place(relx=0.73, rely=0.7, height=26, width=67)

    root.mainloop()


def settings_add():
    root = Tk()
    root.title("Settings:Search subreddits")
    root.geometry("300x100+420+166")
    label = Label(root, text="Search for new subreddits")
    label.pack(side=TOP)
    e = Entry(root)
    e.place(relx=0.15, rely=0.20, relheight=0.30, relwidth=0.65)

    def callback():
        msg = e.get().split(',')
        temp2 = open('./temp1.sh', 'wb')
        with open('./add.sh', 'r') as f:
            for line in f:
                if line.startswith("python "):
                    line = line.strip()
                    for i in range(0, len(msg)):
                        line = line + " " + msg[i]
                    line = line + "\n"
                temp2.write(bytes(line))
        #temp1.write(bytes("\n chmod a+x temp.sh", "utf-8"))
        temp2.close()
        #shutil.move("./temp1.txt", "./temp.sh")
        subprocess.call("chmod a+x temp1.sh", shell=True)
        # Calling the collect bash script
        subprocess.call("./temp1.sh", shell=True)
        root.destroy()

    def callbackerr():
        root.destroy()
    b = Button(root, text="SEARCH", command=callback)
    b.place(relx=0.05, rely=0.7, height=26, width=67)
    c = Button(root, text="CLOSE", command=callbackerr)
    c.place(relx=0.73, rely=0.7, height=26, width=67)

    root.mainloop()


def go(canvas, query):
    getMemeList(query)
    imageList = m.memeList
    if imageList is not None:
        # diplay 1st image
        display(canvas, imageList[0])
        print('display done')
    else:
        print('No matches')


def prev(canvas):
    m.currentImage = (m.currentImage - 1) % len(m.memeList)
    display(canvas, m.memeList[m.currentImage])


def next(canvas):
    m.currentImage = (m.currentImage + 1) % len(m.memeList)
    display(canvas, m.memeList[m.currentImage])


if __name__ == '__main__':
    import meme_gui
    meme_gui.vp_start_gui()
