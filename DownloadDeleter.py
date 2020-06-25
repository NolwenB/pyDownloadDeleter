import getpass, os, time

# init variables
def delete_input():
    canDelete = input("Delete these files? (y/n): ").upper()
    if canDelete == "Y":
        return True
    elif canDelete == "N":
        return False
    print("Try again dawg.")
    return delete_input()
delete_time = 172800 # TWO DAYS IN SECONDS

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
file_amount = 0
for b in paths:
    print("\t")
    for a in onlyfiles:
        if (time.time()-os.path.getmtime(b+a) >= delete_time):
            file_amount += 1
            print(f"** {a}")
print(f"Amount of files: {file_amount}")
# Asks users if the files can be deleted
if file_amount == 0 or not delete_input():
    quit()

for b in paths:
    print("\t")
    for a in onlyfiles:
        if (time.time()-os.path.getmtime(b+a) >= delete_time):
            os.remove(b+a)