# In class work
# Date: 10/19/21
done = False
while not done:  # The operator not yields True if its argument is false, False otherwise
    entry = int(input('Please enter a number, odd if you want to finish: '))
    if entry % 2 != 0:
        done = True
    else:
        print(entry)
