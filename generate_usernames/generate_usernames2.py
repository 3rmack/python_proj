import sys
import collections


def process_line(line, usernames):
    fields = line.split(":")
    #print(fields)
    username = generate_username(fields, usernames)
    user = User(username, fields[FORENAME], fields[MIDDLENAME], fields[SURNAME], fields[ID])
    #print(user)
    return user


def generate_username(fields, usernames):
    username = (fields[FORENAME][0] + fields[MIDDLENAME][:1] + fields[SURNAME]).replace("-", "").replace("'", "")
    username = original_name = username[:8].lower()
    count = 1
    while username in usernames:
        username = "{0}{1}".format(original_name, count)
        count += 1
    usernames.add(username)
    #print(usernames)
    return username


def print_users(users):
    namewidth = 17
    usernamewidth = 9
    lines = []
    head1 = "{0:<{nw}} {1:^6} {2:{uw}}".format("Name", "ID", "Username", nw=namewidth, uw=usernamewidth)
    head2 = "{0:-<{nw}} {0:-<6} {0:-<{uw}}".format("", nw=namewidth, uw=usernamewidth)
    for key in sorted(users):
        user = users[key]
        initial = ""
        if user.middlename:
            initial = " " + user.middlename[0]
        name = "{0.surname}, {0.forename}{1}".format(user, initial, nw=namewidth)  # формируем строку имени
        name = "{0:<.{nw}}".format(name, nw=namewidth)  # урезаем строку
        #print(name)
        lines.append(("{0:.<{nw}} ({1.id:4}) {1.username:{uw}}".format(name, user, nw=namewidth, uw=usernamewidth)))  # сохраняем все строки вывода с список
    lcount = 0
    print("{0}  {0}".format(head1))
    print("{0}  {0}".format(head2))
    for i in range(0, len(lines), 2):  # цикл только с четными числами
        print("{0}  {1}".format(lines[i], lines[i+1]))  # вызываем и печатаем элементы из списка парами
        lcount += 1
        if lcount == 10:
            print('\f')
            lcount = 0
            print("{0}  {0}".format(head1))
            print("{0}  {0}".format(head2))
        #print(lines[i]+" "+lines[i+1])


def main():
    if len(sys.argv) == 1 or sys.argv[1] in {"-h", "--help"}:
        print("usage: {0} filel [file2 [... fileN]]".format(sys.argv[0]))
        sys.exit()
    usernames = set()
    users = {}
    for filename in sys.argv[1:]:
        for line in open(filename, encoding="utf8"):
            line = line.rstrip()
            if line:
                user = process_line(line, usernames)
                #print(user)
                users[(user.surname.lower(), user.forename.lower(), user.id)] = user
                #print(users)
    #print(users)
    print_users(users)

ID, FORENAME, MIDDLENAME, SURNAME, DEPARTMENT = range(5)
User = collections.namedtuple("User", "username forename middlename surname id")
main()
