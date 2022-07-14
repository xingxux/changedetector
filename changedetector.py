version_file = open("history/last", "r")
last = int(version_file.read())

last_file = open("history/" + last, "r")
print(last_file)

