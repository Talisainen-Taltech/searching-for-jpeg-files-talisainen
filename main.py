'''
1. Text files
JSON, XML, TXT, PY, C, INI, YAML, CSV, RTF
2. Binary files
DOC, XLS, DOCS, JPEG, MP3, ZIP, EXE, PDF

OPEN,

open(filename)

WRITE - w
APPEND - a+
READ - r+

rb
wb
ab
'''
import os
import zipfile


for i in range(10,200):
    filename = "file%d" %i
    f= open('random_files/'+filename, 'rb').read(3)
    if f == (b'\xff\xd8\xff'):
        os.rename('random_files/' + filename, 'random_files/' + filename + ".jpg")
    else:
        os.remove('random_files/' + filename)

