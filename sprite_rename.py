import os
import sys

directory = sys.argv[1]
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        newname = filename.replace('.png.png', '.png')
        newname = newname[6:]
        os.rename(os.path.join(directory, filename), os.path.join(directory, newname))