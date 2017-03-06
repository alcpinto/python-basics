names = ['Jeff', 'Gary', 'Jill', 'Samantha']

for name in names:
    statement = 'Hello there, ' + name
    print(statement)

print(', '.join(names))


who = 'Gary'
how_many = 12

print('{} bought {} apples today!'.format(who, how_many))


location_of_files = '/home/abilio'
file_name = 'DataScience-test.pem'

import os

with open(os.path.join(location_of_files, file_name)) as f:
    print(f.read())

