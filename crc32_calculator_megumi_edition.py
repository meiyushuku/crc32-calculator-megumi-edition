import binascii # [1]
import os # [2]
import math # [3]
import time # [4]
import re # [5]
import csv
import codecs # [6]
import sys
# Import module of CRC-32[1], system[2], math[3], time[4], regular expression[5], and character encoding[6].

version = str("1.3.05")

file_name_exclude = [".gitattributes", ".gitignore", "desktop.ini", "thumbs.db"]
file_ext_exclude = [".py"]
# For file_filter_list_dir(), file_filter_walk().

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
    print("#          ...        .=+=-=***-: . .:**+=+-==.           # Use the rapid command below to start a task:")
    print("#          ..          :=:--======:::.--.====:            # ")
    print("#         ..            ==-=-::.--::..:...::.             # cal -v: Vanish mode.")
    print("#        -:.   .    .:=****+:...::.....   :==:            # cal -t: Create report as text file with readability.")
    print("#        +*=:-+=:-=*#******=.......       =+**+:          # cal -c: Create report as CSV file for Microsoft Excel.")
    print("#       -*******##*********=.   ::..     :+*****=         # cal -b: Create the text and CSV file both.")
    print("#       +******##########***-::-+=-=:.: :+++*****         # ")
    print("#       -*****##########**+*+=:-+:+..-+=*+++*****         # help: View details.")
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

def info_page1():
    print("")
    print("Execution modes below are porvided:")
    print("")
    print("Scan modes")
    print("I. Current directory only")
    print("II. Tree traversal (including all sub folders)")
    print("")
    print("Output modes")
    print("1. Vanish mode: the calculation result of CRC-32 are only displayed on screen.")
    print("2. Text file: create report as text file with readability.")
    print("3. CSV file: create report as CSV file for Microsoft Excel.")
    print("4. Both: create the text and CSV file both.")
    print("")
    print("The folder named crc_report will be created (if none) in current directory and reports will be saved to there.")
    print("The report file will be named with system time converted to UTC+0 in ISO 8601 format.")
    print("")
    print("Files and folders below have been excluded by default:")
    print("")
    print("desktop.ini")
    print("thumbs.db")
    print(".gitattributes")
    print(".gitignore")
    print(".py")
    print(".git")
    print("crc_report")
    print("")
    print("You can also add custom file extension exclusions with a command.")
    print("")
    input("Next >>> ")
    info_page2()

def info_page2():
    print("")
    print("Command list:")
    print("")
    print("cal -v: Scan with mode I and output with mode 1.")
    print("cal -t: Scan with mode I and output with mode 2.")
    print("cal -c: Scan with mode I and output with mode 3.")
    print("cal -b: Scan with mode I and output with mode 4.")
    print("cal --walk-v: Scan with mode II and output with mode 1.")
    print("cal --walk-t: Scan with mode II and output with mode 2.")
    print("cal --walk-c: Scan with mode II and output with mode 3.")
    print("cal --walk-b: Scan with mode II and output with mode 4.")
    print("add -ex: Add custom file extension exclusions.")
    print("")
    input("Menu >>> ")
    print("")
    return start()

def mode_switch():                                                                     
    try:
        user_input_menu_ori = input("########################################################### Type here >>> ")
        global scan_mission, output_mission
        user_input_menu = user_input_menu_ori.strip()
        if user_input_menu == "cal -v":
            scan_mission = 100
            output_mission = 60
            return
        elif user_input_menu == "cal -t":
            scan_mission = 100
            output_mission = 70
            return
        elif user_input_menu == "cal -c":
            scan_mission = 100
            output_mission = 80
            return
        elif user_input_menu == "cal -b":
            scan_mission = 100
            output_mission = 90
            return
        elif user_input_menu == "cal --walk-v":
            scan_mission = 200
            output_mission = 60
            return
        elif user_input_menu == "cal --walk-t":
            scan_mission = 200
            output_mission = 70
            return
        elif user_input_menu == "cal --walk-c":
            scan_mission = 200
            output_mission = 80
            return
        elif user_input_menu == "cal --walk-b":
            scan_mission = 200
            output_mission = 90
            return
        elif user_input_menu == "help":
            info_page1()
        elif user_input_menu == "add -ex":
            #custom_ext_exclude()
        elif user_input_menu == "show -ex":
            print("########################################################### %s" % file_ext_exclude)
            return mode_switch()
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
            root_compare = root + "\\"
            if not root_compare.find(".\\.git\\"): # Found
                pass
            elif "crc_report\\" in root_compare:
                pass
            else:
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
        result = crc_core(file_name) # [2]
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
            if output_mission == 60:
                return
            elif output_mission == 70:
                outputer_txt()
                return
            elif output_mission == 80:
                outputer_csv()
                return
            elif output_mission == 90:
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

def crc_core(file_name):
    try:
        block_size = 1024 * 64 # Def size of buffer block.
        block_count = 0 # Processed Blocks
        block_count_total = math.ceil(file_size / block_size) # All Blocks
        with open(file_name, "rb") as file:
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
        report_folder = ".\\crc_report"
        if not os.path.isdir(report_folder):
            os.mkdir(report_folder)
        writer = codecs.open(".\\crc_report\\" + txt_name + ".txt", "a","utf-8")
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
        csv_list.append(str('"%s"' % file_size_dis)) # column3
        csv_list.append(str('"CRC-32: %08X"' % result)) # column4
        csv_list.append(str('"%s"' % time_stamp)) # column5
        report_folder = ".\\crc_report"
        if not os.path.isdir(report_folder):
            os.mkdir(report_folder)
        if file_count == 1:
            writer = codecs.open(".\\crc_report\\" + csv_name + ".csv", "a","utf-8")
            writer.write("Path,File,Size,Value,Timestamp\n")
        else:
            writer = codecs.open(".\\crc_report\\" + csv_name + ".csv", "a","utf-8")
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
                writer.write("{:s},{:s},{:s},{:s},{:s}".format(
                csv_list[0],
                csv_list[1],
                csv_list[2],
                csv_list[3],
                csv_list[4]
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
    if scan_mission == 100:
        file_filter_list_dir()
    elif scan_mission == 200:
        file_filter_walk()
    for file_name in file_name_list:
        file_name_abs = os.path.abspath(file_name)
        # For display() and outputer_?().
        file_size = os.path.getsize(file_name)
        # For file_size_filter(), display() and crc_core().
        file_size_class = file_size_filter(file_size)
        file_count += 1
        display()
        # Global var below:
        # file_name, file_name_abs, file_size, file_size_class
    ##################################################################
    ### Next: display() -> crc_core() -> display() -> outputer_?() ###
    ##################################################################

    if file_count == 0:
        print("No file which need to be calculated in this folder.")
        print("Use the command below to do something or exit by any other.")
    else:
        print("Task is completed. Use the command below to do something or exit by any other.")
    print("")
    print("menu: Return to menu.")
    print("")
    user_input_end_ori = input("Type here >>> ")
    user_input_end = user_input_end_ori.strip()
    if user_input_end == "menu":
        pass
    else:
        sys.exit()