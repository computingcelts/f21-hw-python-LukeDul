# In class work
# Date: 10/19/21
done = False
while not done:
    entry = int(input('Please enter a number, even if you want to finish: '))
    if entry % 2 == 0:
        done = True
    else:
        print(entry)
