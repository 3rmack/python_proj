import os
import sys


path = "."


class ExitError(Exception): pass


def main():
    file_list = get_file_list()
    print_output(file_list)
    while True:
        user_input = get_user_input("Choose filename: ")
        process_user_input(user_input, file_list)


def get_file_list():
    file_list = []  # создаем пустой список для хранения названия файлов
    file_list_temp = os.listdir(path)  # получаем список файлов во временный список
    for file_name in file_list_temp:  # обходим все элементы временного списка
        if file_name.endswith("lst"):  # ищем все названия, заканчивающиеся на .lst
            file_list.append(file_name)  # удаляем все називания, не заканчивающиеся на ".lst"
    return file_list


def print_output(file_list):
    for i in range(len(file_list)):
        print("{0}: {1}".format(i+1, file_list[i]))  # выводим названия файлов как по ТЗ


def get_user_input(message):
    user_input = input(message)
    return user_input


def process_user_input(user_input, file_list):
    try:
        if int(user_input) == 0:
            raise ExitError
        if 0 < int(user_input) <= len(file_list):
            file = open(file_list[int(user_input)-1])
            for string in file:
                print(string, end="")
            print()
        else:
            print("No such file")
    except ValueError:
        if user_input in file_list:
            file = open(user_input)
            for string in file:
                print(string, end="")
            print()
        else:
            print("No such file")
    except ExitError:
        print("Exiting...")
        sys.exit()


main()
