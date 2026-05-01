def divisible6(n):
    if n%6==0:
        return True
    else:
        return False
    
a=[1,2,1456,654685,65465,648964,645555,6,12]

f=list(filter(divisible6, a))
print(f)