import os

def file_filter_list_dir():
    global path_abs
    global file_count
    global file_count_total
    global file_name_abs_list
    path_abs = os.path.abspath(".")
    file_count = 0
    file_count_total = 0
    file_name_abs_list = list()
    for file in os.listdir(path_abs):
        file_name_abs = os.path.join(path_abs, file)
        if os.path.isfile(file_name_abs):
            file_name_abs = file
            file_size = os.path.getsize(file_name_abs)
            # For filtering unnecessary files.
            if file_size != 0:
                if str(os.path.splitext(file_name)[1]) == ".py":
                    pass
                elif str(file_name) == ".gitattributes":
                    pass
                elif str(file_name) == ".gitignore":
                    pass
                elif str(os.path.splitext(file_name)[1]) == ".exe":
                    pass
                elif str(file_name) == "desktop.ini":
                    pass
                elif str(file_name) == "Thumbs.db":
                    pass
                else:
                    file_count_total += 1
                    file_name_abs = os.path.join(path_abs, file_name)
                    file_name_abs_list.append(file_name_abs))

55555555555555555555555
file_filter_list_dir()
for file_name_abs in file_name_abs_list:
    file_size = os.path.getsize(file_name_abs) 
    # For file_size_filter(), display() and crc_core().
    file_count += 1
    print(file_name_abs)