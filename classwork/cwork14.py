# In class work
# Date: 11/9/21

fruit = ['orange', 'apple', 'pear', 'banana', 'lemon']  # list because of [], mutable

vowels = ['a', 'e', 'i', 'o', 'u']

index = 0

print(fruit)

for element in fruit:
    if element[0] in vowels:  # in is a keyword that can iterate through a containers
        fruit[index] = element.upper()
        print(element.upper())
    index += 1

print(fruit)
