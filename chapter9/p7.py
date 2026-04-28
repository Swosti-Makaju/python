with open("chapter9/log.txt") as f:
    lines = f.readlines()

lineno = 1
found = False

for line in lines:
    if "python" in line:
        print(f"python is present in the log file. line no: {lineno}")
        found = True
    lineno += 1

if not found:
    print("python is not present in the log file.")