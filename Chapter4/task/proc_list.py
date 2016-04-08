import os
import sys


path = "."


class ExitError(Exception): pass


class BackError(Exception): pass


def main():
    file_list_temp = os.listdir(path)  # получаем список файлов во временный список
    file_list = list(file_name for file_name in file_list_temp if file_name.endswith(".lst"))  # используем генератор списков для создания списка файлов, оканчивающихся на ".lst"
    while True:
        if len(file_list) == 0:  # если список пуст (нет файлов), то выполняется "инициализация"
            print("List is empty")
            user_input = get_user_input(2)
            if user_input:
                if user_input in "Aa":
                    user_input = input("Enter filename: ")
                    if not user_input.endswith(".lst"):
                        user_input += ".lst"
                    add_item_to_list(user_input, file_list)
                elif user_input in "Qq":
                    sys.exit("Exit")
                else:
                    return
        else:
            print_output(file_list)
            user_input = get_user_input(3)
            try:
                user_input = int(user_input)
                process_user_input_int(user_input, file_list)
            except ValueError:
                process_user_input_str(user_input, file_list)


def print_output(file_list):
    file_list = sorted(file_list)
    for i in range(len(file_list)):
        print("{0}: {1}".format(i+1, file_list[i]))  # выводим названия файлов как по ТЗ


def get_user_input(input_type):
    if input_type == 1:
        user_input = input("Enter filename: ")
        return user_input
    elif input_type == 2:
        user_input = input("[A]dd [Q]uit: ")
        available_input = "AaQq"
        if user_input in available_input:
            return user_input
        else:
            print("Invalid choice, select one of '{0}'".format(available_input))
            return
    elif input_type == 3:
        user_input = input("[R]ead [A]dd [D]elete [S]ave [Q]uit: ")
        available_input = "RrAaDdSsQq"
        if user_input in available_input:
            return user_input
        else:
            print("Invalid choice, select one of '{0}'".format(available_input))
    elif input_type == 4:
        user_input = input("Enter number or filename: ")
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
        if user_input in "Dd":
            user_input_2 = get_user_input(1)
            try:
                if not user_input_2.endswith(".lst"):
                    user_input_2 += ".lst"
                file_list.remove(user_input_2)
            except ValueError:
                print("No such file")
                return
        elif user_input in "Qq":
            raise ExitError
        elif user_input in "Rr":
            user_input_2 = get_user_input(4)
            try:
                user_input_2 = int(user_input_2)
                process_user_input_int(user_input_2, file_list)
            except ValueError:
                if not user_input_2.endswith(".lst"):
                    user_input_2 += ".lst"
                if user_input_2 in file_list:
                    print_file(user_input_2)
        elif user_input in "Ss":
            save_list(file_list)
        elif user_input in "Aa":
            user_input_2 = get_user_input(1)
            if not user_input_2.endswith(".lst"):
                user_input_2 += ".lst"
                add_item_to_list(user_input_2, file_list)
            else:
                #print_output(file_list)
                return
    except ExitError:
        sys.exit("Exit")
    # except BackError:
    #     print("-- no items are in the list --")
    #     return


def print_file(user_input):
    if os.stat(user_input).st_size == 0:
        print("-- file is empty --")
    else:
        file = open(user_input)
        for i, line in enumerate(file):
            if line:
                print("{0}: {1}".format(i+1, line), end="")
        print()


def add_item_to_list(user_input, file_list):
    print("Adding {0} to list...".format(user_input))
    file_list.append(user_input)


def save_list(file_list):
    print("Saving...")
    for file in file_list:
        try:
            os.stat(file).st_size
        except FileNotFoundError:
            print("File {0} not found. Creating...".format(file))
            new_file = open(file, "w")
            new_file.write("")
            new_file.close()


main()
