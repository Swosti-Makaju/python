subject1=float(input("enter marks of subject 1:"))
subject2=float(input("enter marks of subject 2:"))
subject3=float(input("enter marks of subject 3:"))

total_percentage=(subject1+subject2+subject3)/3

if(total_percentage>=40) and (subject1>=33 and subject2>=33 and subject3>=33):
    print("pass")
else:
    print("fail")