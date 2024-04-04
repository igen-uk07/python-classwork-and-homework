def greet_users(first_name, last_name):
    print(f'{first_name} {last_name}')
    print('welcome abroad')

greet_users("john", "smith")# positional argument
greet_users(last_name= "smith", first_name="john") #keyword argument = doest not worry about postion

#use keyword argument after positional argument