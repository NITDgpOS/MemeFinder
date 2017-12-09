import sys
from os import listdir
from os.path import isfile, join

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

from PIL import Image, ImageTk

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

def getMemeList(source):
	paths = [f for f in listdir(source) if isfile(join(source, f))]
	finalPath= [source+'/'+p for p in paths]
	print(finalPath)
	return finalPath

class memes:
	def __init__(self):
		self.memeList= getMemeList('gui_test')
		self.currentImage= 0

m= memes()

def display(canvas, image_path):
	x= Image.open(image_path)
	print('x working')
	gif1 = ImageTk.PhotoImage(image= x.resize((400,400),Image.ANTIALIAS))
	canvas.create_image(5,10, image = gif1)
	canvas.gif1=gif1

def go(canvas):
	imageList= m.memeList
	# diplay 1st image
	display(canvas, imageList[0])
	print('display done')
	return imageList

def prev(canvas):
	currentImage= (currentImage-1)%len(m.memeList)
	prevImage= memeList[currentImage]
	display(canvas, prevImage)

def next(canvas):
	currentImage= m.currentImage
	currentImage= (currentImage+1)%len(m.memeList)
	nextImage= m.memeList[currentImage]
	m.currentImage=currentImage
	display(canvas, nextImage)


if __name__ == '__main__':
    import meme_gui
    meme_gui.vp_start_gui()


