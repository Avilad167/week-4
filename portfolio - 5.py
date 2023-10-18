def cel_to_fah(celsius):
    f = (celsius * 9/5) + 32
    return f
def fah_to_cel(fahrenheit):
    c = (fahrenheit - 32) * 5/9
    return c
celsius = int (input("enter the temp in celsius:"))
fahrenheit = int (input("enter the temp in fahrenheit:"))
convert_fahrenheit = cel_to_fah(celsius)
print("temp in fahrenheit is:", convert_fahrenheit)
convert_celsius = fah_to_cel(fahrenheit)
print("temp in celsius is:", convert_celsius)

