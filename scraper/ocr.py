from PIL import Image
import pytesseract
from pytesseract import image_to_string
import os
import cv2
import re
from autocorrect import spell
import string
from models import *

db_pre_ocr = db('pre_ocr')
db_post_ocr = db('post_ocr')


def extractText(image_path):
    try:
        image = cv2.imread(image_path)
        if image is None:
            return "00000"
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.threshold(
            gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        gray = cv2.medianBlur(gray, 3)

        # write the grayscale image to disk as a temporary file so we can
        # apply OCR to it
        filename = "scraper/{}.png".format(os.getpid())
        cv2.imwrite(filename, gray)

        # load the image as a PIL/Pillow image, apply OCR, and then delete
        # the temporary file
        text = pytesseract.image_to_string(Image.open(filename))
        os.remove(filename)
        text = text.strip().split()
        chars_to_remove = ['.', '!', ':']
        extracted = list()
        for t in text:
            for c in chars_to_remove:
                t = t.replace(c, '')
            extracted.append(spell(t))
        return(' '.join(extracted))

    except BaseException as e:
        print(e)


try:
    process_files = db_pre_ocr.find({})

    for image in process_files:
        fromImage = extractText(image['location'])
        fromImageClean = re.sub(r'\W+', ' ', fromImage)  # Only alphanumeric
        if fromImage != "00000":

            add_image = {
                'location': image['location'],
                'attributes': image['attributes'],
                'ocr_out': fromImageClean
            }
            db_post_ocr.insert_one(add_image)
except BaseException as e:
    print(e)
