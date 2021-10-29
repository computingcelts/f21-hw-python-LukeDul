# Get tree height from user
height = int(input('Enter height of tree: '))

count = 0
# prints the increasing portion of the pyramid
while count < height:
    print('*' * count)
    count += 1
# prints the decreasing portion of the pyramid by decreasing the amount of * until we reach zero
while count > 0:
    print('*' * count)
    count -= 1

