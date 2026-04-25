text=input("enter comments:").lower()
if  ( "make a lot of money" in text or "become rich" in text or "earn a lot of money" in text):
    print("This is a spam comment")
else:
    print("This is not a spam comment") 