from os import listdir
from os.path import isfile, join
from os import walk
import getpass
# Creates / Reads the paths.txt file in the same directory as the py file
# By default, if there is not a file, the delete path is the user's downloads folder
try:
    pathsTXT = open("paths.txt", "r")
except:
    pathsTXT = open("paths.txt","w+")
    pathsTXT.write(f"C:\\Users\\{getpass.getuser()}\\Downloads\\")
    pathsTXT = open("paths.txt", "r")

paths = pathsTXT.read().split("\n")

onlyfiles = [f for f in listdir(paths[0]) if isfile(join(paths[0], f))]

print(*onlyfiles, sep="\n-- ")
print(f"** {len(onlyfiles)} items")