course = 'python for beginners'
 # len is a general urpose func
print(len(course))
 # when a func belongs to something or is speific to some king of obj we refer that func as  methods
  # upper is a method bcoz this func belongs to strings
print(course.upper()) # this metyhod does not chnage orginal string it modifies string and returns it
print(course.lower())

print(course.find('for')) # return index of first
print(course.replace('beginners', 'Absolue beginners'))
print(course.replace('p', 'A'))
print('python' in course) # its produces booloean value
print('Python' in course)