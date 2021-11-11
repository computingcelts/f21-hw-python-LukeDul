# In class work
# Date: 11/11/15
import pprint

d = {}

d['Italy'] = 'Rome'
d['France'] = 'Paris'
d['Spain'] = 'Madrid'
d['Mexico'] = 'CDX'

print(d)

d['Spain'] = ['Madrid', 'Barcelona']

print(d)

for country, cities in d.items():
    print('key: ', country, 'and value: ', cities)

print()  # these are loops do the exact same thing

for x in d.items():
    print('key: ', x[0], 'and value: ', x[1])

