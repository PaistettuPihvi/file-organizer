import os
import sys

mainfolder = str("/home/"+os.getlogin())
folder1 = False
folder2 = False
folder3 = False 
folder4 = False
folder5 = False
said = 0
photoext = ".png", ".jpg", ".jpeg", ".svg"
videoext = ".mp4", ".avi", ".flv", ".gif", ".wmv", ".webm"


if os.path.exists(mainfolder+"/Downloads"):
    print("Downloads file found")
else:
    os.system("mkdir "+mainfolder+"/Downloads")
    print("Downloads folder created")
    #Python
if os.path.exists(mainfolder + "/python"):
    print("Python folder found")
    folder1 = True
else:
    os.system("mkdir "+mainfolder+"/python")
    print("Python folder created")

    
    #Photos
if os.path.exists(mainfolder + "/photos"):
    print("Photos folder found")
    folder2 = True
else:
    os.system("mkdir "+mainfolder+"/photos")
    print("Photos folder created")
    
    
    #Videos
if os.path.exists(mainfolder + "/videos"):
    print("Videos folder found")
    folder3 = True
else:
    os.system("mkdir "+mainfolder+"/videos")
    print("Videos folder created")


    #Scripts
if os.path.exists(mainfolder + "/scripts"):
    print("Scripts folder found")
    folder4 = True
else:
    os.system("mkdir "+mainfolder+"/scripts")
    print("Scripts folder created")


    #Executables
if os.path.exists(mainfolder + "/executables"):
    print("Executables folder found")
    folder5 = True
else:
    os.system("mkdir "+mainfolder+"/executables")
    print("Executables folder created   ")

if folder1 == True:
    if folder2 == True:
        if folder3 == True:
            if folder4 == True:
                if folder5 == True:
                    clear = input("Remove folders? [y/n] ")

                    if clear == "y":
                        os.system("rm -r "+mainfolder+"/python")
                        os.system("rm -r "+mainfolder+"/photos")
                        os.system("rm -r "+mainfolder+"/videos")
                        os.system("rm -r "+mainfolder+"/scripts")
                        os.system("rm -r "+mainfolder+"/executables")
                        print("All folders removed.")  
                        sys.exit()  

run = True
print("Looking for folders.")
while run:
    for files in os.listdir(mainfolder+"/Downloads"):
        if files.endswith(".py"):
            f = files.split()
            if os.path.exists(mainfolder+"/python/"+f[0]) == True:
                print(f[0]+" already exists")
            else:
                os.system("sudo mv "+mainfolder+"/Downloads/"+f[0]+" "+mainfolder+"/python")
                print(f[0]+" Moved to Python folder")
        if files.endswith(photoext):
            f = files.split()
            if os.path.exists(mainfolder+"/photos/"+f[0]) == True:
                print(f[0]+" already exists")
            else:
                os.system("sudo mv "+mainfolder+"/Downloads/"+f[0]+" "+mainfolder+"/photos")
                print(f[0] +" moved to Photos folder")
        #elif said < 1:
            #print("Downloads folder does not contain any movable files.")
           #said =+ 1
        if files.endswith(videoext):
            f = files.split()
            if os.path.exists(mainfolder+"/videos/"+f[0]) == True:
                print(f[0]+ "already exists")
            else:
                os.system("sudo mv "+mainfolder+"/Downloads/"+f[0]+" "+ mainfolder+"/videos")
                print(f[0]+ " moved to Videos folder")
        if files.endswith(".sh", ".bat"):
            f = files.split()
            if os.path.exists(mainfolder+"/scripts/"+f[0]) == True:
                print(f[0] + " already exists")
            else:
                os.system("sudo mv "+mainfolder+"/Downloads/"+f[0]+" "+mainfolder+"/scripts")
                print(f[0]+ " moved to Scripts folder")
        if files.endswith(".exe", ".jar"):
            f = files.split()
            if os.path.exists(mainfolder+"/executables/"+f[0]) == True:
                print(f[0] + " already exists")
            else:
                os.system("sudo mv "+mainfolder+"/Downloads/"+f[0]+" "+mainfolder+"/executables")
                print(f[0]+ " moved to Executables folder")