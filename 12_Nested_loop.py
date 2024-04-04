for x in range(4):
    for y in range(3):
        print(f'({x},{y})')


for i in range(2):
    print('x' * 5)
    for j in range(2):
        print('x' * 2)



numbers = [5,2,5,2,2]
for x_count in numbers:
    print('x' * x_count)
    

numbers = [5,2,5,2,2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)    
