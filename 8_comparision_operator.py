'''temperature  = 35

if temperature > 30:
    print("ïts a hot day")
else:
    print("ïts not a hot day")'''

name = input('Enter your Name : ')
if len(name) < 3:
    print("Name must be atleast 3 characters ..")
elif len(name) > 50:
    print("Name can be of maximum of 50 characters")
else:
    print("Name loooks good !")