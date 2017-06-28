from os import listdir
from os.path import isfile, join, getctime
mypath = '/home/kirill/Programming/Python/Book/library/email/'
onlyfiles = [(mypath+f, getctime(mypath+f)) for f in listdir(mypath) if isfile(join(mypath, f))]
onlyfiles = sorted(onlyfiles, key=lambda file: file[1])
print onlyfiles

