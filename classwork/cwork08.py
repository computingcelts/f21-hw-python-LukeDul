# In class work
# Date: 10/19/21
done = False
while not done:
    entry = int(input('Please enter a number, positive if you want to finish: '))
    if entry > 0:
        done = True
    else:
        print(entry)
