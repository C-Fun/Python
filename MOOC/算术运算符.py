fullname = input("Enter a full name:")
n = fullname.rfind(" ")
m = fullname.find(" ")
print("Last name:",fullname[n+1:])
print("First name:",fullname[:m])
