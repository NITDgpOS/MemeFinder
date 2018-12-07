import hashlib
from os import listdir
from os.path import isfile, join
import subprocess
import time
import shutil
from models import *
import encodings

db = db('pre_ocr')
source = 'raw/'
destination = 'processed/'
raw_files = [f for f in listdir(source) if isfile(join(source, f))]

print("%d files in raw" % (len(raw_files)))
for f in raw_files:
    ''' Renames scrapped images and and moves to processed folder '''
    fname = f
    fname = ''.join([i if ord(i) < 128 else ' ' for i in fname])
    pfile = hashlib.sha256((str(time.time()) + f).hexdigest()
    ext = f.split('.')[-1]
    location = "{}{}.{}".format(destination, pfile, ext)
    shutil.move("{}{}".format(source, f), location)
    files_data = {
    	'location' : location,
    	'attributes' : fname.split('.')[:-1]
    }
    db.insert_one(files_data)