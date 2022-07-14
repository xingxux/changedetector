version_file = open("history/last", "r")
last_file = open("history/" + version_file.read().strip(), "r")
print(read(last_file))

