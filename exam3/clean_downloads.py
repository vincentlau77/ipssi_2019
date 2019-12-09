#!/usr/bin/python3

import sys
import os
from datetime import datetime
from datetime import timedelta

def clean_downloads(path):
    list_files = os.listdir(path)
    strToPrintForDel = "cleanup old files: (more than 10 days + 50MB)"
    strToPrintForMove = "organizing other files:"
    filesToDel = []
    filesToMove = []
    for aFile in list_files:
        if os.stat(path+aFile).st_size > 1000000:
            filesToDel.append(aFile)
            continue
        else:
            dateOfFile = datetime.fromtimestamp(os.stat(path+aFile).st_mtime)
            tenDayOfDiff = (datetime.now())+timedelta(days=-10)
            print(dateOfFile)
            if dateOfFile < tenDayOfDiff:
                filesToDel.append(aFile)
                continue
            else:
                filesToMove.append(aFile)
                continue

    if len(filesToDel) > 0:
        print(strToPrintForDel)
        for aFileToDel in filesToDel:
            print("os.remove('"+path+aFileToDel+"')")
    if len(filesToMove) > 0:
        print(strToPrintForMove)
        for aFileToMove in filesToMove:
            # print(aFileToMove)
            dateOfFileForFolder = datetime.fromtimestamp(os.stat(path+aFileToMove).st_mtime).strftime("%Y-%m")
            pathToCreate = path+str(dateOfFileForFolder)
            print(pathToCreate)
            if not os.path.exists(path+str(dateOfFileForFolder)+"/"+aFileToMove):
                os.makedirs(path+str(dateOfFileForFolder)+"/"+aFileToMove)
            print(dateOfFileForFolder)
            print("os.replace('"+path+aFileToMove+"', '"+path+str(dateOfFileForFolder)+"/"+aFileToMove+"')")
    # return filesToMove

if __name__ == "__main__":
    print(clean_downloads(sys.argv[1]))
