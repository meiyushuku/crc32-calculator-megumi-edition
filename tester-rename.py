import os

file_name_exclude = [".gitattributes", ".gitignore", "readme.md", "desktop.ini", "thumbs.db"]
file_ext_exclude = [".py"]

path = "."
file_count = 0
file_count_total = 0
file_name_list = list()

i = 1

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
                os.rename(file_name, "./" + str(i) + ".png")
                i += 1
                print(file_name)

file_name_str = str("123457.png")

print(file_name_str.find("669D487D"))