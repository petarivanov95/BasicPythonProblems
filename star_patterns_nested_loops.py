# The problems below are a variety of problems on nested loops as worked on through the printing of problems related to star-pattern printing. The idea for them was taken from the book Starting out with Python by Tony Gaddis

xrow = 4
yrow = 4

for x in range(xrow):
    for y in range(yrow):
        print("*",end=" ")
    print()
print()

### -----------------------

for x in range(xrow):
    for y in range(x+1):
        print("*", end = "")
    print()
print()

### -----------------------

# program 4-20 from Gaddis/ page 176

for x in range(xrow):
    for y in range(x):
        print(" ",end = " ")
    print("#")
print()

### -----------------------

# problem 13 from Gaddis/page182

for x in range(xrow,0,-1):
    for y in range(x):
        print("*",end=" ")
    print()
print()

### -----------------------

# problem 14 from Gaddis/page 182

for x in range(xrow):
    print("#",end=" ")
    for y in range(x):
        print(" ",end = " ")
    print("#")
