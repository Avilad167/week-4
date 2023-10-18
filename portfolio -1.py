def number (a):
    return (0 <= a <= 100)
a = int(input("enter a number: "))
if number(a):
    print("True")
else:
    print("False")
