temperatures = []
while True:
    string = input("Enter a temperature in degrees Celsius(when completed press double enter): ")
    if not string:
        break  
    if string[-1] == "C":
        celsius = float(string[:-1])
        temperatures.append(celsius)
    else:
        print("Invalid input")
if not temperatures:
    print("No temperatures provided.")
else:   
    max = max(temperatures)
    min = min(temperatures)
    mean = sum(temperatures) / len(temperatures)
    print(" the highest temp:", max)
    print(" the lowest temp:", min)
    print(" the avg temp:", mean)
