import os

path_abs = os.path.abspath(".")
file_name_abs = os.path.join(path_abs, ".gitattributes")

print("")
print(file_name_abs)
print("")
print(os.path.split(file_name_abs)[1])
print("")
print(os.path.split(file_name_abs)[1]).lower())
print("")

#print(startswith(os.path.split(file_name_abs)))