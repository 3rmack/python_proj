class MyException(Exception):
    message = 'Item greater than 4 Error'

    def __str__(self):
        return 'I am a magic method'


def process_item(i):
    if i > 4:
        print i
    else:
        raise MyException


my_list = [1, 56, -6, 0, -1, 35, -234, 534, -2, -4, -5, 432, 1, 0, 6]
for item in my_list:
    try:
        process_item(item)
    except MyException as err:
        print err.message
        print str(err) + '!!!'
