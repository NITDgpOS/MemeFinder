import sys
from os import listdir
from os.path import isfile, join
from search import *

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



class memes:
	def __init__(self):
		self.memeList= ['nofile']
		self.currentImage= 0

m= memes()


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
	# paths = [f for f in listdir(source) if isfile(join(source, f))]
	# finalPath= [source+'/'+p for p in paths]
	# print(finalPath)
	# return finalPath
	source='data3.txt'
	m.memeList= getScore(create_index(source), generateQuery(query))


def display(canvas, image_path):
	x= Image.open(image_path)
	gif1 = ImageTk.PhotoImage(image= x.resize((300,300),Image.ANTIALIAS))
	canvas.create_image(200,150, image = gif1)
	canvas.gif1=gif1

def go(canvas, query):
	getMemeList(query)
	imageList= m.memeList
	if imageList!= None:
		# diplay 1st image
		display(canvas, imageList[0])
		print('display done')
	else:
		print('No matches')

def prev(canvas):
	m.currentImage= (m.currentImage-1)%len(m.memeList)
	display(canvas, m.memeList[m.currentImage])

def next(canvas):
	m.currentImage= (m.currentImage+1)%len(m.memeList)
	display(canvas, m.memeList[m.currentImage])



if __name__ == '__main__':
    import meme_gui
    meme_gui.vp_start_gui()


