import getpass, os, time, shutil

def delete_input():
    canDelete = input("Delete these files/folder? (y/n): ").upper()
    if canDelete == "Y":
        return True
    elif canDelete == "N":
        return False
    print("Try again dawg.")
    return delete_input()
def set_time(minutes=0, hours=0, days=0):
    return (minutes*60) + (hours*3600) + (days*86400)
# init variables
DELETE_TIME = set_time(0, 2) # Two hours

# Creates / Reads the paths.txt file in the same directory as the py file
# By default, if there is not a file, the delete path is the user's downloads folder
try:
    pathsTXT = open("paths.txt", "r")
except:
    pathsTXT = open("paths.txt","w+")
    pathsTXT.write(f"C:\\Users\\{getpass.getuser()}\\Downloads\\")
    pathsTXT = open("paths.txt", "r")

paths = pathsTXT.read().split("\n")

# Formats the path correctly if there is not a '\' at the end of the path
for x in range(len(paths)):
    try:
        if paths[x][-1] != "/" or paths[x][-1] != "\\":
            paths[x] += "\\"
    except:
        pass

# puts all file names in the directories into a list
onlyfiles = [f for f in os.listdir(paths[0]) if os.path.isfile(os.path.join(paths[0], f))]
#onlyfolders = [[x[0] for x in os.walk(directory)]]

# [0] == Directory ~ [1] == Folders ~ [2] == Files
items = next(os.walk(paths[0]))
items[2].remove("desktop.ini")
file_amount = 0
folder_amount = 0
for a in paths:
    print("\t")
    for b in items[2]:
        if (time.time()-os.path.getmtime(a+b) >= DELETE_TIME):
            file_amount += 1
            print(f"** {b}")
    for c in items[1]:
        if (time.time()-os.path.getmtime(a+c+"\\") >= DELETE_TIME):
            folder_amount += 1
            print(f"~~ {c}\\")
print(f"Amount of files: {file_amount}")
print(f"Amount of folders: {folder_amount}")
# Asks users if the files can be deleted
if file_amount + folder_amount == 0 or not delete_input():
    quit()

for a in paths:
    print("\t")
    for b in items[2]:
        if (time.time()-os.path.getmtime(a+b) >= DELETE_TIME):
            os.remove(a+b)
    for c in items[1]:
        if (time.time()-os.path.getmtime(a+c+"\\") >= DELETE_TIME):
            shutil.rmtree(a+c+"\\")
