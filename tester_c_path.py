import os

file_name_exclude = [".gitattributes", ".gitignore", "desktop.ini", "thumbs.db"]
file_ext_exclude = [".py", ".exe"]

def file_filter_walk():
    global file_count, file_count_total, file_name_list
    #global path_abs
    try:
        path = "."
         #path_abs = os.path.abspath(path)
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
        print("Error code: 100")

#######################
file_filter_walk()
for file_name in file_name_list:
    file_size = os.path.getsize(file_name) 
    # For file_size_filter(), display() and crc_core().
    #file_size_class = file_size_filter(file_size)
    file_count += 1
    file_name_abs = os.path.abspath(file_name)
    print("{}/{}".format(file_count, file_count_total))
    print("Path: %s" % os.path.split(file_name_abs)[0])
    print("File: %s" % os.path.split(file_name_abs)[1])
    print("")

input()