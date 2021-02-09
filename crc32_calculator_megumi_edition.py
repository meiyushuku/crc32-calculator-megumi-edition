import binascii # [1]
import os # [2]
import math # [3]
import time # [4]
import re # [5]
import csv
import codecs # [6]
import sys
# Import module of CRC-32[1], system[2], math[3], time[4], regular expression[5], and character encoding[6].

version = str("1.3.0")

file_name_exclude = [".gitattributes", ".gitignore", "desktop.ini", "thumbs.db"]
file_ext_exclude = [".py", ".exe"]

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
    print("#         ..            ==-=-::.--::..:...::.             # cal n: Calculate and display only.")
    print("#        -:.   .    .:=****+:...::.....   :==:            # cal r: Create report with readability.")
    print("#        +*=:-+=:-=*#******=.......       =+**+:          # cal e: Create report for Microsoft Excel.")
    print("#       -*******##*********=.   ::..     :+*****=         # cal b: Both create.")
    print("#       +******##########***-::-+=-=:.: :+++*****         # ")
    print("#       -*****##########**+*+=:-+:+..-+=*+++*****         # info: View details.")
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
    mode_switch()

def info():
    print("Testing...\nPress enter or type any to return menu.")
    input()
    return start()

def mode_switch():                                                                     
    try:
        user_input_menu_ori = input("########################################################### Type here: ")
        global scan_mission
        global output_mission
        user_input_menu = user_input_menu_ori.strip()
        if user_input_menu == "cal n":
            scan_mission = 1000
            output_mission = 600
            return
        elif user_input_menu == "cal r":
            scan_mission = 1000
            output_mission = 700
            return
        elif user_input_menu == "cal e":
            scan_mission = 1000
            output_mission = 800
            return
        elif user_input_menu == "cal b":
            scan_mission = 1000
            output_mission = 900
            return
        elif user_input_menu == "cal an":
            scan_mission = 2000
            output_mission = 600
            return
        elif user_input_menu == "cal ar":
            scan_mission = 2000
            output_mission = 700
            return
        elif user_input_menu == "cal ae":
            scan_mission = 2000
            output_mission = 800
            return
        elif user_input_menu == "cal ab":
            scan_mission = 2000
            output_mission = 900
            return
        elif user_input_menu == "info":
            info()
        elif user_input_menu == "":
            print("########################################################### Not entered.")
            return mode_switch()
        else:
            print("########################################################### Command is not defined.")
            return mode_switch()
    except:
        print("Error code: 108")

def file_filter_list_dir():
    global file_count, file_count_total, file_name_list
    try:
        path = "."
        file_count = 0
        file_count_total = 0
        file_name_list = list()
        for file in os.listdir(path):
            if os.path.isfile(os.path.join(path, file)):
                file_name = file
                file_size = os.path.getsize(file_name) 
                # For filtering unnecessary files.
                if file_size != 0:
                    if str(file_name).lower() in file_name_exclude:
                        pass
                    elif str(os.path.splitext(file_name)[1]).lower() in file_ext_exclude:
                        pass
                    else:
                        file_count_total += 1
                        file_name_list.append(file_name)
    except:
        print("Error code: 100")

def file_filter_walk():
    global file_count, file_count_total, file_name_list
    try:
        path = "."
        file_count = 0
        file_count_total = 0
        file_name_list = list()
        for root, dirs, files in os.walk(path):
            for file in files:
                file_name = os.path.join(root, file)
                file_size = os.path.getsize(file_name) 
                # For filtering unnecessary files.
                if file_size != 0:
                    if str(os.path.split(file_name)[1]).lower() in file_name_exclude:
                        pass
                    elif str(os.path.splitext(os.path.split(file_name)[1])[1]).lower() in file_ext_exclude:
                        pass
                    else:
                        file_count_total += 1
                        file_name_list.append(file_name)
    except:
        print("Error code: 109")

def display():
    global file_size_dis, result, time_stamp
    try:
        print("{}/{}".format(file_count, file_count_total))
        print("Path: %s" % os.path.split(file_name_abs)[0])
        print("File: %s" % os.path.split(file_name_abs)[1])
        if file_size_class == 1:  
            file_size_dis = str("{:d} Bytes".format(file_size))
            print("Size: %s" % file_size_dis)
        elif file_size_class == 2:
            file_size_dis = str("{:d} Bytes ({:d} KiB)".format(
                file_size,
                file_size >> 10
                )
            )
            print("Size: %s" % file_size_dis)
        elif file_size_class == 3:
            file_size_dis = str("{:d} Bytes ({:d} MiB)".format(
                file_size,
                file_size >> 20
                )
            )
            print("Size: %s" % file_size_dis)
        elif file_size_class == 4:
            file_size_dis = str("{:d} Bytes ({:.2f} GiB)".format(
                file_size,
                file_size / pow(1024, 3)
                )
            )
            print("Size: %s" % file_size_dis)
        # Get file name and size for display before calculating CRC-32.
        time_start = time.time() # [1]
        result = crc_core(file_name_abs) # [2]
        timeEnd = time.time() # [3]
        print("Elapsed time: {:.2f} s".format(timeEnd - time_start)) # [4]
        print("CRC-32: %08X" % result) # [5]
        time_stamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(timeEnd)) # [6]
        print("Timestamp: %s\n" % time_stamp) # [7]
        # [1] Get beginning time.
        # [2] Get result of CRC-32.
        # [3] Get ending time.
        # [4] Display elapsed time.
        # [5] Display result of CRC-32.
        # [6] Creat time_stamp by [3].
        # [7] Display time_stamp.
        ########################
        ### Output Workspace ###
        ########################
        try:
            if output_mission == 600:
                return
            elif output_mission == 700:
                outputer_txt()
                return
            elif output_mission == 800:
                outputer_csv()
                return
            elif output_mission == 900:
                outputer_txt()
                outputer_csv()
                return
        except:
            print("Error code: 105")
            return 0
        ########################
        return
    except:
        print("Error code: 103")

def crc_core(file_name_abs):
    try:
        block_size = 1024 * 64 # Def size of buffer block.
        block_count = 0 # Processed Blocks
        block_count_total = math.ceil(file_size / block_size) # All Blocks
        with open(file_name_abs, "rb") as file:
            str = file.read(block_size)
            crc = 0
            while len(str) != 0:
                if block_count % 1377 == 1:
                    time_speed_reference = time.perf_counter_ns()
                else:
                    pass
                crc = binascii.crc32(str, crc) & 0xffffffff
                str = file.read(block_size)
                block_count += 1
                if file_size_class == 1:
                    if block_count % 1 == 0 or block_count == block_count_total: 
                        print("\rProcessed: {:d}/{:d} Bytes ({:.2f}%)".format(
                            file_size,
                            file_size,
                            block_count / block_count_total * 100
                            ), end=""
                        )
                elif file_size_class == 2:
                    if block_count % 1 == 0 or block_count == block_count_total: 
                        print("\rProcessed: {:d}/{:d} KiB ({:.2f}%)".format(
                            file_size >> 10,
                            file_size >> 10,
                            block_count / block_count_total * 100
                            ), end=""
                        )
                elif file_size_class == 3:
                    if block_count % 1377 == 0 or block_count == block_count_total: 
                        print("\rProcessed: {:d}/{:d} MiB ({:.2f}%)".format(
                            block_count >> 4,
                            file_size >> 20,
                            # Mean: block_count * 1024 * 64 >> 20
                            # Mean: file_size / 1024 / 1024
                            # Keywords: bitwise operation, arithmetic shift
                            block_count / block_count_total * 100
                            ), end=""
                        )
                elif file_size_class == 4:
                    if block_count % 1377 == 0 or block_count == block_count_total:
                        time_speed_now = time.perf_counter_ns()
                        time_speed_delta = time_speed_now - time_speed_reference
                        if block_count == block_count_total:
                            print("\rProcessed: {:.2f}/{:.2f} GiB ({:.2f}%) Speed: - MiB/s".format(
                                block_count / pow(2, 14),
                                file_size / pow(2, 30),
                                block_count / block_count_total * 100
                                ), end=""
                            )
                        else:  
                            print("\rProcessed: {:.2f}/{:.2f} GiB ({:.2f}%) Speed: {:.0f} MiB/s".format(
                                block_count / pow(2, 14),
                                file_size / pow(2, 30),
                                block_count / block_count_total * 100,
                                1377 * pow(2, -4) * pow(10, 9) / time_speed_delta
                                ), end=""
                            )
            print(" ")
            return crc
    except:
        print("Error code: 101")
        return 0

def file_size_filter(file_size):
    try:
        if file_size < 1024: # Byte
            file_size_class = 1
        elif file_size < 1048576: # KiB
            file_size_class = 2
        elif file_size < 1073741824: # MiB
            file_size_class = 3
        elif file_size < 1099511627776: # GiB
            file_size_class = 4
        return file_size_class
    except:
        print("Error code: 102")

def outputer_txt():
    try:
        writer = codecs.open(txt_name + ".txt", "a","utf-8")
        writer.write("Path: %s\n" % os.path.split(file_name_abs)[0])
        writer.write("File: %s\n" % os.path.split(file_name_abs)[1])
        writer.write("Size: %s\n" % file_size_dis)
        writer.write("CRC-32: %08X\n" % result)
        if file_count == file_count_total:
            writer.write("Timestamp: %s" % time_stamp)
        else:
            writer.write("Timestamp: %s\n\n" % time_stamp)
        writer.close()
        return
    except:
        print("Error code: 106")

def outputer_csv():
    try:
        csv_list = list()
        csv_list.append(str('"%s"' % os.path.split(file_name_abs)[0])) # column1
        csv_list.append(str('"%s"' % os.path.split(file_name_abs)[1])) # column2
        csv_list.append(str("%s" % file_size_dis)) # column3
        csv_list.append(str("CRC-32: %08X" % result)) # column4
        csv_list.append(str("%s" % time_stamp)) # column5
        writer = codecs.open(csv_name + ".csv", "a","utf-8")
        if file_count != file_count_total:
            writer.write("{:s},{:s},{:s},{:s},{:s}\n".format(
                csv_list[0],
                csv_list[1],
                csv_list[2],
                csv_list[3],
                csv_list[4]
                )
            )
        else:
                writer.write("{:s},{:s},{:s},{:s}".format(
                csv_list[0],
                csv_list[1],
                csv_list[2],
                csv_list[3]
                )
            )
        writer.close()
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
### Next: menu() -> mode_switch() ##
####################################

    #####################################
    ### Output Files Naming Workspace ###
    #####################################
    iso_8601 = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime(time.time()))
    txt_name = str("%s" % iso_8601)
    csv_name = str("%s" % iso_8601)

    #######################
    ### Traversal Start ###
    #######################
    if scan_mission == 1000:
        file_filter_list_dir()
    elif scan_mission == 2000:
        file_filter_walk()
    for file_name in file_name_list:
        file_name_abs = os.path.abspath(file_name)
        file_size = os.path.getsize(file_name_abs)
        # For file_size_filter(), display() and crc_core().
        file_size_class = file_size_filter(file_size)
        file_count += 1
        display()
        # Global var: file_name_abs, file_size, file_size_class
    ##################################################################
    ### Next: display() -> crc_core() -> display() -> outputer_?() ###
    ##################################################################

    if file_count == 0:
        print("No file in this folder. Use the command below to do something or exit by any other press.")
    else:
        print("Task is completed. Use the command below to do something or exit by any other press.")
    print("")
    print("menu: Return to menu.")
    print("")
    user_input_end_ori = input("Type here: ")
    user_input_end = user_input_end_ori.strip()
    if user_input_end == "menu":
        pass
    else:
        sys.exit()