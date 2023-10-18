def rmvchar(string):
    if len(string) > 1:
        return string[:-1]
    else:
        return string
string = input(str("enter the string:"))
result= rmvchar(string)
print("after removal", result)

