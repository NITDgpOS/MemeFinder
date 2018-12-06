from PIL import Image
import pytesseract
from pytesseract import image_to_string
import os
import cv2
import os
from autocorrect import spell
import string

with open('database/database.txt', 'r') as fread, open('database/data2.txt', 'a+') as fwrite:
    def extract_text(image_path):
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
            filename = "{}.png".format(os.getpid())
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
                    t = string.replace(t, c, '')
                extracted.append(spell(t))
            return(' '.join(extracted))

        except BaseException:
            print("image skipped")

    try:
        count = 0
        for line in fread:
            if count > 0:
                image_location = line.split(',')[0]
                fromImage = extract_text(image_location)
                if fromImage != "00000":
                    fwrite.write(
                        line[:-1] + "," + ''.join([i if ord(i) < 128 else "" for i in fromImage]) + "\n")
            else:
                fwrite.write(line[:-1] + ", ocr_out\n")
            print(count)
            count = count + 1
    except BaseException:
        print("image skipped")
