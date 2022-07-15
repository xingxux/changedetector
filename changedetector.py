# get last generated PDF file
last_version = int(open("history/last", "r").read().strip())
last_file = open("history/" + str(last_version), "r")

# generate new PDF file
new_file = open("history/" + str(last_version+1), "w")
new_file.write("abc\n")
new_file.close()

# TODO: compare new_file to the last_file, detect changes, fire alarm etc.

# update newly generated file as "last"
version_file = open("history/last", "w")
version_file.write(str(last_version+1)+"\n")
version_file.close()

