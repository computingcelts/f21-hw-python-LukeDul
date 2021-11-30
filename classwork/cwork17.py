# In class work
# Date: 11/30/21

# Error Handling: Try and Except
# Error Classes

list1 = [3, 5, 6]
d = {'Texas': 10, 'Arizona': 20}

try:
    val = int(input('Please enter a small positive integer: '))

    print('You entered :', val)
    print('Element at', val, ':', list1[val])
    print('The value of Texas is ', d['texas'])

except IndexError:
    print('Index invalid.')

except ValueError:
    print('Input not accepted.')

except KeyError:
    print('The key does\'nt exist.')

print('Work done.')
