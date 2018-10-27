'''
Modified: MakeToast(Yoojin Choi, Ella) (maketoastyj@gmail.com)
'''
import os
import tempfile
import subprocess

class OCR :
    def ocr(self, path):
        temp = tempfile.NamedTemporaryFile(delete=False)

        process = subprocess.Popen(['tesseract', path, temp.name], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        process.communicate()

        with open(temp.name + '.txt', 'r') as handle:
            contents = handle.read()

        os.remove(temp.name + '.txt')
        os.remove(temp.name)

        return contents

OCR = OCR()
str = OCR.ocr('path/to/image')
print(str)
