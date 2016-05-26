k = input('Input k: ')
number = 0
count = 0
while True:
    for item in str(number):
        if int(item) in [0, 5]:
            ignore = False
        else:
            ignore = True
            break
    if not ignore:
        count += 1
    if count == k:
        print number
        break
    number += 5
