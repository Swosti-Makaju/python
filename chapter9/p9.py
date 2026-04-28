with open("chapter9/file.txt") as f:
    content1=f.read()

    with open("chapter9/log.txt") as f:
       content2=f.read()

    if(content1==content2):
            print("both the files are identical")
    else:         
            print("both the files are different")