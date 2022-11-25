x = int(input())
y = int(input())
z = int(input())

if ((not (x or y or z)) == ((not x) and (not y) and (not y))):
    print('True')
else:
    print('False')
