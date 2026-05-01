files = ["1.txt", "2.txt", "3.txt"]

for file in files:
    try:
        f = open(file, "r")
        print(f"{file} opened successfully.")
        f.close()
    except FileNotFoundError:
        print(f"{file} is not present. Please create it.")