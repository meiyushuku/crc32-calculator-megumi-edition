import os

def file_filter_list_dir():
    global path_abs, file_count, file_count_total, file_name_abs_list
    try:
        path_abs = os.path.abspath(".")
        file_count = 0
        file_count_total = 0
        file_name_abs_list = list()
        for file in os.listdir(path_abs):
            if os.path.isfile(os.path.join(path_abs, file)):
                file_name_abs = os.path.join(path_abs, file)
                file_size = os.path.getsize(file_name_abs) 
                # For filtering unnecessary files.
                if file_size != 0:
                    file_name_exclude = [".gitattributes", ".gitignore", "desktop.ini", "thumbs.db"]
                    file_ext_exclude = [".py", ".exe"]
                    if str(os.path.split(file_name_abs)[1]).lower() in file_name_exclude:
                        pass
                    elif str(os.path.splitext(os.path.split(file_name_abs)[1])[1]).lower() in file_ext_exclude:
                        pass
                    else:
                        file_count_total += 1
                        file_name_abs_list.append(file_name_abs)
    except:
        print("Error code: 100")

#######################
file_filter_list_dir()
for file_name_abs in file_name_abs_list:
    file_size = os.path.getsize(file_name_abs) 
    # For file_size_filter(), display() and crc_core().
    #file_size_class = file_size_filter(file_size)
    file_count += 1
    print(file_name_abs)