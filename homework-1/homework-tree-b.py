# Get tree height from user
height = int(input('Enter height of tree: '))
# used to increment height while still being able to use height in the loop condition
height_increment = height
# init count
count = 0
# prints the increasing portion of the pyramid
while count < height:
    if height_increment != height:  # removes extra spaces at the beginning
        print(' ' * height_increment, '*' * count)
    count += 1
    height_increment -= 1
# prints the decreasing portion of the pyramid
while count > 0:
    if height_increment != height:  # removes extra spaces at the end
        print(' ' * height_increment, '*' * count)
    count -= 1
    height_increment += 1
