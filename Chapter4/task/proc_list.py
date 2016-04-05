import os
import sys


path = "."


class ExitError(Exception): pass


class BackError(Exception): pass


def main():
    file_list_temp = os.listdir(path)  # получаем список файлов во временный список
    file_list = list(file_name for file_name in file_list_temp if file_name.endswith(".lst"))  # используем генератор списков для создания списка файлов, оканчивающихся на ".lst"
    print_output(file_list)
    while True:
        user_input = get_user_input(1)
        try:
            user_input = int(user_input)
            process_user_input_int(user_input, file_list)
        except ValueError:
            process_user_input_str(user_input, file_list)


def print_output(file_list):
    for i in range(len(file_list)):
        print("{0}: {1}".format(i+1, file_list[i]))  # выводим названия файлов как по ТЗ


def get_user_input(input_type):
    if input_type == 1:
        user_input = input("Choose filename: ")
    if input_type == 2:
        user_input = input("[A]dd [Q]uit: ")
        avaliable_input = "AaQq"
        if user_input in avaliable_input:
            return user_input
        else:
            print("Invalid choise, select one of '{0}'".format(avaliable_input))
    if input_type == 3:
        user_input = input("[A]dd [D]elete [S]ave [Q]uit: ")
    return user_input


def process_user_input_int(user_input, file_list):
    try:
        if int(user_input) == 0:
            raise ExitError
        if 0 < int(user_input) <= len(file_list):
            filo = file_list[int(user_input)-1]
            print_file(filo)
        else:
            raise BackError
    except ExitError:
        sys.exit("Exit")
    except BackError:
        print("-- no items are in the list --")
        return


def process_user_input_str(user_input, file_list):
    try:
        if user_input in file_list:
            print_file(user_input)
        else:
            user_input_2 = get_user_input(2)
            if user_input_2 in "Aa":
                if not user_input.endswith(".lst"):
                    user_input = user_input+".lst"
                print(user_input)
                new_file = open(user_input, "w")
                new_file.write("")
                new_file.close()
                file_list.append(user_input)
                print_output(file_list)
            else:
                print_output(file_list)
                return
    except ExitError:
        sys.exit("Exit")
    except BackError:
        print("-- no items are in the list --")
        return


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
