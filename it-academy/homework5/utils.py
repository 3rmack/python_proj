import math


def read_file(file_name):
    with open(file_name) as file_in:
        data = file_in.readlines()
        return data[0].split()


def write_file(file_name, data):
    with open(file_name, 'w') as file_out:
        result = ''
        for item in data:
            result += str(item) + ' '
        file_out.write(result)


def circle_area(data):
    result = []
    for item in data:
        result.append(math.pi*int(item)**2)
    return result
