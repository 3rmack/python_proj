import os
import sys


path = "."


class ExitError(Exception): pass


def main():
    file_list = get_file_list()
    print_output(file_list)
    while True:
        user_input = get_user_input(1, file_list)
        process_user_input(user_input, file_list)


def get_file_list():
    file_list_temp = os.listdir(path)  # получаем список файлов во временный список
    file_list = list(file_name for file_name in file_list_temp if file_name.endswith(".lst"))  # используем
    # генератор списков для создания списка файлов, оканчивающихся на ".lst"
    return file_list


def print_output(file_list):
    for i in range(len(file_list)):
        print("{0}: {1}".format(i+1, file_list[i]))  # выводим названия файлов как по ТЗ


def get_user_input(input_type, file_list):
    if input_type == 1:
        user_input = input("Choose filename: ")
        # process_user_input(user_input, file_list)
    if input_type == 2:
        user_input = input("[A]dd [Q]uit: ")
    if input_type == 3:
        user_input = input("[A]dd [D]elete [S]ave [Q]uit: ")
    return user_input


def process_user_input(user_input, file_list):
    try:
        if int(user_input) == 0:
            raise ExitError
        if 0 < int(user_input) <= len(file_list):
            filo = file_list[int(user_input)-1]
            print_file(filo)
        else:
            print("-- no items are in the list --")
    except ValueError:
        if user_input in file_list:
            print_file(user_input)
        else:
            print("-- no items are in the list --")
    except ExitError:
        print("Exiting...")
        sys.exit()


def print_file(user_input):
    if os.stat(user_input).st_size == 0:
        print("-- file is empty --")
    else:
        file = open(user_input)
        for i, line in enumerate(file):
            if line:
                print("{0}: {1}".format(i+1, line), end="")
        print()


main()
