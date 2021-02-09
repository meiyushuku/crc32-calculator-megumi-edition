import binascii # [1]
import os # [2]
import math # [3]
import time # [4]
import re # [5]
import csv
import codecs # [6]
import sys
# Import module of CRC-32[1], system[2], math[3], time[4], regular expression[5], and character encoding[6].

version = str("1.2.15")

def start():
    try:
        try: input = raw_input
        except NameError: pass
        menu()
        print("########################################################### Scanning...")
        print("")
    except:
        print("Error code: 104")  

def menu():
    cmdList = ["cal n", "cal r", "cal e", "cal b", "info"]
    #print("                           ........:::..                   ")
    #print("                         ....:::::::::...                  ")
    print("               ############################################ ")
    print("                                                          # ")
    print("                        .::::::::::::..                   # ")
    print("                       .:::-=+*#####*=:                   # ")
    print("                      .::=*#*++#######*=.                 # ")
    print("                     .:-*##*=:=#####**++=-                # ")
    print("#                     :+**=::=####*+----:==.                ")
    print("#                     -+=::-*###*++==-=::--=:               ")
    print("#                     ..:-=***##++*=+=+---=-+-              CRC-32 Calculator Megumi Edition")
    print("#                 ..  .:-+##==**+==+==-+=+*--+              ")
    print("#                ..:::-+**#+=---==:-+***+**=-=.             Version %s (2021)" % version)
    print("#               ..::. +#***=+**:...:=++-**+*--:             ")
    print("#              .....  =*#*++=++.    .--.=+*#=+..            ")
    print("#             .....   :+**#-.::...  ....++*#+*-.          # ")
    print("#             .  .    .=**#*=.....     :***+**:.          # ")
    print("#           ..        :=*++*#+.  .::  :**++-++:.          # ")
    print("#          ...        .=+=-=***-: . .:**+=+-==.           # Use the rapid command below to start a task.")
    print("#          ..          :=:--======:::.--.====:            # ")
    print("#         ..            ==-=-::.--::..:...::.             # %s: Calculate and display only." % cmdList[0])
    print("#        -:.   .    .:=****+:...::.....   :==:            # %s: Create report with readability." % cmdList[1])
    print("#        +*=:-+=:-=*#******=.......       =+**+:          # %s: Create report for Microsoft Excel." % cmdList[2])
    print("#       -*******##*********=.   ::..     :+*****=         # %s: Both create." % cmdList[3])
    print("#       +******##########***-::-+=-=:.: :+++*****         # ")
    print("#       -*****##########**+*+=:-+:+..-+=*+++*****         # %s: View details." % cmdList[4])
    print("#                                                         # ")
    #print("         .=+*******+++***++++:-=..=:=*+++++*****+          ")
    #print("                      ***+++:--=.=-==**+++******=          ")
    #print("                     :****==.+.=:--=-**+********-          ")
    #print("                     .****- -::--:::-+*********+           ")
    #print("                     :**#*-:=:=-.   .=*****##**-           ")
    #print("                     :+##*-=++-- ....+*****#**+.           ")
    #print("                     .*##+=*+-:-.::::==******+:            ")
    #print("                     .*##**=--::::::---+****+-             ")
    #print("                     -###*=----:-:::----***++              ")
    #print("                     +##%=-----::--:-===*%**+.             ")
    #print("               .... .+###=------:----===+%%#*=             ")
    #print("              -=+++=+###*+-----------=-=*%%%#*:            ")
    #print("             :+*****######+==-=------=*#+#####+            ")
    #print("           .=#*+##%%###*+*###*******###++=*####=           ")
    #print("          -+*##*#*%###*++=-==+++++****##++=*****:          ")
    #print("         -:=+**###*##**===:--:----==*+#**=+=****+          ")
    #print("          .=+*+**#*#**=--:-.:  ::-++*=##+::=+***+-         ")
    #print("          :=+=*+**##*+--: :.:   ..=**-+#+::--*+++=         ")
    modeSwitch()

def info():
    print("Testing...\nPress enter or type any to return menu.")
    input()
    return start()

def modeSwitch():                                                                     
    try:
        userInputStartOri = input("########################################################### Type here: ")
        global mainMission
        userInputStart = userInputStartOri.strip()
        if userInputStart == "cal n":
            mainMission = 600
            return
        elif userInputStart == "cal r":
            mainMission = 700
            return
        elif userInputStart == "cal e":
            mainMission = 800
            return
        elif userInputStart == "cal b":
            mainMission = 900
            return
        elif userInputStart == "info":
            info()
        elif userInputStart == "":
            print("########################################################### Not entered.")
            return modeSwitch()
        else:
            print("########################################################### Command is not defined.")
            return modeSwitch()
    except:
        print("Error code: 108")

def fileFilterListdir():
    global path
    global fileCount
    global fileCountTotal
    global fileNameList
    try:
        path = "."
        fileCount = 0
        fileCountTotal = 0
        fileNameList = list()
        # Global var: fileCount, fileCountTotal, fileNameList
        for file in os.listdir(path):
            filePathName = os.path.join(path, file)
            if os.path.isfile(filePathName):
                fileName = file
                fileSize = os.path.getsize(fileName) 
                # For filtering unnecessary files.
                if fileSize != 0:
                    if str(os.path.splitext(fileName)[1]) == ".py":
                        pass
                    elif str(os.path.splitext(fileName)[0]) == ".gitattributes":
                        pass
                    elif str(os.path.splitext(fileName)[0]) == ".gitignore":
                        pass
                    elif str(os.path.splitext(fileName)[1]) == ".exe":
                        pass
                    elif str(os.path.splitext(fileName)[1]) == ".db":
                        pass
                    else:
                        fileCountTotal += 1
                        fileNameList.append(fileName)
    except:
        print("Error code: 100")

def crcDisplay():
    global fileSizeDis
    global result
    global timeStamp
    try:
        print("{}/{}".format(fileCount, fileCountTotal))
        print("File: %s" % fileName)
        if fileSizeClass == 1:  
            fileSizeDis = str("Size: {:d} Bytes".format(fileSize))
            print(fileSizeDis)
        elif fileSizeClass == 2:
            fileSizeDis = str("Size: {:d} Bytes ({:d} KiB)".format(
                fileSize,
                fileSize >> 10
                )
            )
            print(fileSizeDis)
        elif fileSizeClass == 3:
            fileSizeDis = str("Size: {:d} Bytes ({:d} MiB)".format(
                fileSize,
                fileSize >> 20
                )
            )
            print(fileSizeDis)
        elif fileSizeClass == 4:
            fileSizeDis = str("Size: {:d} Bytes ({:.2f} GiB)".format(
                fileSize,
                fileSize / pow(1024, 3)
                )
            )
            print(fileSizeDis)
        # Get file name and size for display before calculating CRC-32.
        timeStart = time.time() # [1]
        result = crcCore(fileName) # [2]
        timeEnd = time.time() # [3]
        print("Elapsed time: {:.2f} s".format(timeEnd - timeStart)) # [4]
        print("CRC32: %08X" % result) # [5]
        timeStamp = time.strftime("Timestamp: %Y-%m-%dT%H:%M:%SZ", time.gmtime(timeEnd)) # [6]
        print("%s\n" % timeStamp) # [7]
        # [1] Get beginning time.
        # [2] Get result of CRC-32.
        # [3] Get ending time.
        # [4] Display elapsed time.
        # [5] Displayresult of CRC-32.
        # [6] Creat timestamp by [3].
        # [7] Display timestamp.
        ########################
        ### Output Workspace ###
        ########################
        try:
            if mainMission == 600:
                return
            elif mainMission == 700:
                outputerRead()
                return
            elif mainMission == 800:
                outputerExcel()
                return
            elif mainMission == 900:
                outputerRead()
                outputerExcel()
                return
        except:
            print("Error code: 105")
            return 0
        ########################
        return
    except:
        print("Error code: 103")

def crcCore(fileName):
    try:
        blockSize = 1024 * 64 # Def size of buffer block.
        blockCount = 0 # Processed Blocks
        blockCountTotal = math.ceil(fileSize / blockSize) # All Blocks
        with open(fileName, "rb") as file:
            str = file.read(blockSize)
            crc = 0
            while len(str) != 0:
                if blockCount % 1377 == 1:
                    timeSpeedReference = time.perf_counter_ns()
                else:
                    pass
                crc = binascii.crc32(str, crc) & 0xffffffff
                str = file.read(blockSize)
                blockCount += 1
                if fileSizeClass == 1:
                    if blockCount % 1 == 0 or blockCount == blockCountTotal: 
                        print("\rProcessed: {:d}/{:d} Bytes ({:.2f}%)".format(
                            fileSize,
                            fileSize,
                            blockCount/blockCountTotal*100
                            ), end=""
                        )
                elif fileSizeClass == 2:
                    if blockCount % 1 == 0 or blockCount == blockCountTotal: 
                        print("\rProcessed: {:d}/{:d} KiB ({:.2f}%)".format(
                            fileSize >> 10,
                            fileSize >> 10,
                            blockCount/blockCountTotal*100
                            ), end=""
                        )
                elif fileSizeClass == 3:
                    if blockCount % 1377 == 0 or blockCount == blockCountTotal: 
                        print("\rProcessed: {:d}/{:d} MiB ({:.2f}%)".format(
                            blockCount >> 4,
                            fileSize >> 20,
                            # Mean: blockCount * 1024 * 64 >> 20
                            # Mean: fileSize / 1024 / 1024
                            # Keywords: bitwise operation, arithmetic shift
                            blockCount/blockCountTotal*100
                            ), end=""
                        )
                elif fileSizeClass == 4:
                    if blockCount % 1377 == 0 or blockCount == blockCountTotal:
                        timeSpeedNow = time.perf_counter_ns()
                        timeSpeedDelta = timeSpeedNow - timeSpeedReference
                        if blockCount == blockCountTotal:
                            print("\rProcessed: {:.2f}/{:.2f} GiB ({:.2f}%) Speed: - MiB/s".format(
                                blockCount / pow(2, 14),
                                fileSize / pow(2, 30),
                                blockCount/blockCountTotal*100
                                ), end=""
                            )
                        else:  
                            print("\rProcessed: {:.2f}/{:.2f} GiB ({:.2f}%) Speed: {:.0f} MiB/s".format(
                                blockCount / pow(2, 14),
                                fileSize / pow(2, 30),
                                blockCount/blockCountTotal*100,
                                1377 * pow(2, -4) * pow(10, 9) / timeSpeedDelta
                                ), end=""
                            )
            print(" ")
            return crc
    except:
        print("Error code: 101")
        return 0

def fileSizeFilter(fileSize):
    try:
        if fileSize < 1024: # Byte
            fileSizeClass = 1
        elif fileSize < 1048576: # KiB
            fileSizeClass = 2
        elif fileSize < 1073741824: # MiB
            fileSizeClass = 3
        elif fileSize < 1099511627776: # GiB
            fileSizeClass = 4
        return fileSizeClass
    except:
        print("Error code: 102")

def outputerRead():
    try:
        txtOutput = codecs.open(txtNameRead + ".txt", "a","utf-8")
        txtOutput.write("File: %s\n" % fileName)
        txtOutput.write("%s\n" % fileSizeDis)
        txtOutput.write("CRC32: %08X\n" % result)
        if fileCount == fileCountTotal:
            txtOutput.write("%s" % timeStamp)
        else:
            txtOutput.write("%s\n\n" % timeStamp)
        txtOutput.close()
        return
    except:
        print("Error code: 106")

def outputerExcel():
    try:
        OutputStr1 = str("File: %s" % fileName)
        OutputStr2 = str("%s" % fileSizeDis)
        OutputStr3 = str("CRC32: %08X" % result)
        OutputStr4 = str("%s" % timeStamp)
        OutputStrList = [OutputStr1, OutputStr2, OutputStr3, OutputStr4]
        txtOutput = codecs.open(txtNameExcel + ".txt", "a","utf-8")
        if fileCountTotal == fileCountTotal:
            txtOutput.write("{:s},{:s},{:s},{:s}\n".format(
                OutputStrList[0],
                OutputStrList[1],
                OutputStrList[2],
                OutputStrList[3]
                )
            )
        else:
                txtOutput.write("{:s},{:s},{:s},{:s}\n\n".format(
                OutputStrList[0],
                OutputStrList[1],
                OutputStrList[2],
                OutputStrList[3]
                )
            )
        txtOutput.close()
        return
    except:
        print("Error code: 107")

#######################
### Start from Here ###
#######################
controller = time.time()
while controller: # Mean: while controller != 0
    start()
####################################
### Next: menu() -> modeSwitch() ###
####################################

    #####################################
    ### Output Files Naming Workspace ###
    #####################################
    txtName = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime(time.time()))
    txtNameRead = str("%sR" % txtName)
    txtNameExcel = str("%sE" % txtName)

    #######################
    ### Traversal Start ###
    #######################
    fileFilterListdir()
    for fileName in fileNameList:
        fileSize = os.path.getsize(fileName) 
        # For fileSizeFilter(), crcDisplay() and crcCore().
        fileSizeClass = fileSizeFilter(fileSize)
        fileCount += 1
        crcDisplay()
        # Global var: fileName, fileSize, fileSizeClass
    ######################################################################
    ### Next: crcDisplay() -> crcCore() -> crcDisplay() -> outputer?() ###
    ######################################################################

    if fileCount == 0:
        print("No file in this folder. Use the command below to do something or exit by any other press.")
    else:
        print("Task is completed. Use the command below to do something or exit by any other press.")
    print("")
    print("menu: Return to menu.")
    print("")
    userinputEndOri = input("Type here: ")
    userinputEnd = userinputEndOri.strip()
    if userinputEnd == "menu":
        pass
    else:
        sys.exit()