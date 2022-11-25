x = int(input())
y = int(input())
z = int(input())

if ((not (x or y or z)) == ((not x) or (not y) or (not y))):
    print('True')
else:
    print('False')
