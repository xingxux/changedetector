last_version = int(open("history/last", "r").read().strip())
last_file = open("history/" + str(last_version), "r")
print(last_file.read())

new_file = open("history/" + str(last_version+1), "w")
new_file.write("abc")
new_file.close()

