marks = []

print("Enter marks of 6 students:")
for i in range(6):
    m = int(input())
    marks.append(m)

marks.sort()

print("Marks in sorted order:")
for m in marks:
    print(m, end=" ")