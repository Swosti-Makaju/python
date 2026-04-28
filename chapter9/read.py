f=open("chapter9/poem.txt")

content=f.read()
if("twinkle" in content):
    print("Twinkle is in the poem")
else:
    print("Twinkle is not in the poem")

f.close()