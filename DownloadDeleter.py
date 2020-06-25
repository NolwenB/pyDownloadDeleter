import getpass, os, time
# init variables
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

onlyfiles = [f for f in os.listdir(paths[0]) if os.path.isfile(os.path.join(paths[0], f))]

#print(*onlyfiles, sep="\n-- ")

for b in paths:
    try:
        if b[-1] != "/" or b[-1] != "\\":
            b += "\\"
    except:
        pass
    for a in onlyfiles:
        print(f"** {a} \t\t: {time.time()-os.path.getmtime(b+a)}")
print(f"** {len(onlyfiles)} items")