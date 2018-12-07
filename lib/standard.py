import hashlib
from os import listdir
from os.path import isfile, join
import subprocess
import time
import shutil
from models import *

db = db('pre_ocr')
source = 'raw/'
destination = 'processed/'
raw_files = [f for f in listdir(source) if isfile(join(source, f))]

print("%d files in raw" % (len(raw_files)))
for f in raw_files:
    ''' Renames scrapped images and and moves to processed folder '''
    
    fname = f
    fname = ''.join([i if ord(i) < 128 else ' ' for i in fname])
    f = f.decode('utf-8', 'ignore')
    pfile = hashlib.sha256((str(time.time()) + f).encode('utf-8')).hexdigest()
    ext = f.split('.')[-1]
    location = "%s%s.%s" % (destination, pfile, ext)
    shutil.move("%s%s" % (source, f), location)
    files_data = {
    	'location' : location,
    	'attributes' : fname.split('.')[:-1]
    }
    db.insert_one(files_data)