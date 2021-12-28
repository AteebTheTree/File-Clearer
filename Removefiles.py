import time
import os
import shutil

path = input("Enter path to clear: ")
dayCheck = int(input("Enter days old file should be to keep: "))

if os.path.exists(path):
    print("Path found, doing things")
    ModifiedTime = dayCheck * 24 * 60 * 60
    for root, dirs, files in os.walk(path):
        for name in files:
            filePath = os.path.join(root, name)
            ctime = os.stat(path).st_ctime
            if(ModifiedTime < ctime):
                os.remove(filePath)
        for name in dirs:
            dirPath = os.path.join(root, name)
            ctime = os.stat(path).st_ctime
            if(ModifiedTime < ctime):
                shutil.rmtree(dirPath)
else:
    print("Path not found :(")
