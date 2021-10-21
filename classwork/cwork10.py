# In class work
# Date: 10/21/21

var = 0
count = 0

for i in range(1, 100):
    if i % 2 == 1:
        var += i
        count += 1
print('Count of odd numbers from 1 to 99:', count)
print('Accumulated odd numbers from 1 to 99:', var)
