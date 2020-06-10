print('This is a string {}'.format('INSERT'))

print("The {} {} {}".format('fox', 'brown', 'quick'))
print("The {2} {1} {0}".format('fox', 'brown', 'quick'))

print("The {q} {b} {f}".format(f='fox', b='brown', q='quick'))

# float formatting

result = 100/777

print("The result was {}".format(result))

print("The result was {r}".format(r=result))

print("The result was {r:1.3f}".format(r=result))

name = "Patrick"
age = 30

print("Hi my name is {}".format(name))
print(f"Hi my name is {name}")

print(f"Hi my name is {name}, and I'am {age} years old.")
