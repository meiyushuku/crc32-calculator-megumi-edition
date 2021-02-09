import glob
import os
import re

#filterFiles = list()

#targetPattern = r"*.txt"
#targetPattern2 = r"*.py"

#t = glob.glob(r"*.txt")
#p = glob.glob(r"*.txt")

#filterFiles.append(t)
#filterFiles.append(p)

##########################################################################
##########################################################################

#def diff3(fileNameList, pyFiles, txtFiles):
    #return list(set(fileNameList).
        #symmetric_difference(set(pyFiles)).
        #symmetric_difference(set(txtFiles))
        #)

#def diff2(fileNameList, pyFiles):
    #return list(set(fileNameList).symmetric_difference(set(pyFiles)))

#def diff1(fileNameList, txtFiles):
    #return list(set(fileNameList).symmetric_difference(set(txtFiles)))

#print(diff3(fileNameList, pyFiles, txtFiles))

#print(diff2(fileNameList, pyFiles))

#print(diff1(fileNameList, txtFiles))

##########################################################################
##########################################################################


path = "."

fileCount = 0
fileCountTotal = 0

fileNameList = list()
pyFiles = list()
txtFiles = list()

for file in os.listdir(path):
    filePathName = os.path.join(path, file)
    if os.path.isfile(filePathName):
        fileName = file
        fileSize = os.path.getsize(fileName) 
        if fileSize != 0:
            if str(os.path.splitext(fileName)[1]) == ".py":
                pyFiles.append(fileName)
            elif str(os.path.splitext(fileName)[1]) == ".txt":
                txtFiles.append(fileName)
                pass
            else:
                fileCountTotal += 1
                fileNameList.append(fileName)
                                                                            #ext = os.path.splitext(fileName)
                                                                            #print(os.path.splitext(fileName))
                                                                            #print(os.path.splitext(fileName)[1])
                                                                            #pyFiles = list(glob.glob(r"*.py"))
                                                                            #txtFiles = list(glob.glob(r"*.txt"))
print("")
print(pyFiles)
print(txtFiles)
print("")
for fileName in fileNameList:
    #fileSize = os.path.getsize(fileName) 
    # For fileSizeFilter(), crcDisplay() and crcCore().
    fileCount += 1
    print(fileName)

                                                                            #print("")
                                                                            #print(filterFiles)