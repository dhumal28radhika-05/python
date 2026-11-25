a=int(input("Enter a number:  "))
b=int(input("Enter a number:  "))
c=int(input("Enter a number:  "))
if a==b==c:
    print("side of triangle are equal hence eqilateral triangle")
elif a==b or a==c or b==c :
    print("two sides of triangle are equal hence isosceles triangle")
else:
    print("no sides are equal hence scalene triangle")