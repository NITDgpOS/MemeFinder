import hashlib
from os import listdir
from os.path import isfile, join
import subprocess
import time
import shutil
import models
import encodings

db = models.db('pre_ocr')
source = 'raw/'
destination = 'processed/'
raw_files = [f for f in listdir(source) if isfile(join(source, f))]

print("%d files in raw" % (len(raw_files)))
for f in raw_files:
    ''' Renames scrapped images and and moves to processed folder '''
    fname = f
    fname = ''.join([i if ord(i) < 128 else ' ' for i in fname])
    pfile = hashlib.sha256((str(time.time()) + f).encode('utf-8')).hexdigest()
    ext = f.split('.')[-1]
    location = "{}{}.{}".format(destination, pfile, ext)
    shutil.move("{}{}".format(source, f), location)
    files_data = {
        'location': location,
        'attributes': fname.split('.')[0]
    }
    db.insert_one(files_data)
