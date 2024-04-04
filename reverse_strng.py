def reverse(string):
    l = len(string)
    rev = ""
    for i in range(0,l):
        rev = rev+string[l-i-1]

    print(string)

reverse("nitin")