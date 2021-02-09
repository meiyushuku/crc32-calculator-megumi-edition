import binascii # [1]
import os # [2]
import math # [3]
import time # [4]
import re # [5]
import csv
import codecs # [6]
import sys

def crc32(fileNameInput):
    try:
        fileSize = os.path.getsize(fileNameInput) 
        blockSize = 1024 * 64 # Def size of buffer block.
        blockCount = 0 # Processed Blocks
        blockCountTotal = math.ceil(fileSize / blockSize) # All Blocks
        with open(fileName, "rb") as file:
            str = file.read(blockSize)
            crc = 0
            whileCount = 0
            while len(str) != 0:
                if whileCount % 1377 == 1:
                    timeSpeedReference = time.perf_counter_ns()
                else:
                    pass
                crc = binascii.crc32(str, crc) & 0xffffffff
                str = file.read(blockSize)
                blockCount += 1
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
                whileCount +=1
            print(" ")
        return crc
    except:
        print("compute file crc failed!")
        return 0

path1 = "."
abpath = os.path.abspath(path1)

print(abpath)
fileName = "(画集・設定資料集) [ゆずソフト] 喫茶ステラと死神の蝶 オフィシャルビジュアルファンブック_976217A5.zip"
fileNameInput = os.path.join(abpath, fileName)
print("%s" % fileNameInput)
result = crc32(fileNameInput)
print("CRC32: %08X" % result)
print("")

input()