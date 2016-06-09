# coding: utf-8
my_list = [1, 56, -6, 0, -1, 35, -234, 534, -2, -4, -5, 432, 1, 0, 6]
for i in my_list:
    try:
        if i < -5:
            raise Exception('Я меньше -5')
        else:
            print '!!!{0}!!!'.format(i)
    except Exception as err:
        print err.message
        continue
