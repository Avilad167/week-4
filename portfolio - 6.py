temp = input("enter the temp in celsius along with C:")
if temp[-1] == "C":
    celsius = float(temp[:-1])
    fahrenheit = (celsius * 9/5) + 32
    print(" the equivalent temp in fahrenheit is :", fahrenheit)
else:
    print(" invalid input")
    
