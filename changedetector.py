last_version = int(open("history/last", "r").read().strip())
last_file = open("history/" + str(last_version), "r")
print(last_file.read())

new_file = open("history/" + str(last_version+1), "w")
new_file.write("abc\n")
new_file.close()

version_file = open("history/last", "w")
version_file.write(str(last_version+1)+"\n")
version_file.close()

