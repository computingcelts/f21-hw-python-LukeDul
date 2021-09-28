# In class work
# Date: 9/28/21

# enter value 1(a number) and store it in variable x
x = int(input('Enter first value: '))

# enter value 2(a number) and store it in variable y
y = int(input('Enter second value: '))

# enter value 3(a string) and store it in variable z
z = input('Enter operator: ')

# print the sum of x and y only if the value of z is equal to '+'

print('Inputted operator: ', z)
if z == '+':
    print(x + y)
else:
    if z == '-':
        print(x - y)
    else:
        if z == '*':
            print(x * y)
        else:
            if z == '/':
                print(x / y)
            else:
                print('Invalid arithmetic operator.')


