numbers = [3,4,56,42,2,222]
numbers.append(20)
numbers.insert(0,99) #index,number
numbers.remove(3)
#numbers.pop()
#numbers.clear()
print(numbers.index(56)) # check existence of cahracters
print(0 in numbers) # check existence of cahracters
numbers.sort()
numbers.reverse()
num = numbers.copy()
numbers.append(10)
print(numbers)
print(num)