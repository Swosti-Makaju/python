with open("chapter9/log.txt","r") as f:
    content=f.read()

if("python" in content):
    print("python is present in the log file")
else:
    print("python is not present in the log file")