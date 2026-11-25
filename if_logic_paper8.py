#Check whether a number is a single-digit or double-digit number.
a=int(input("Enter a number:  "))
if a>=0 and a<=9:
    print("the number is  a single digit number")
elif a>9 and a<99:
    print("the number is a double digit number")
else:
    print("the number is not single digit number or double digit number")
