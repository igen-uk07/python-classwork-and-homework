num = [1,2,3,44,4,5,5,6,6,7,7]
unique = []
for number in num:
    if number not in unique:
        unique.append(number)
print(unique)
