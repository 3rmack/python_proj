def create(command):
    spaces[command[0]] = {'parent': command[1], 'vars': []}


def add(command):
    spaces[command[0]]['vars'].append(command[1])


def get(command):
    try:
        if command[1] in spaces[command[0]]['vars']:
            print(command[0])
        else:
            get([spaces[command[0]]['parent'], command[1]])
    except KeyError:
        print(None)


spaces = {'global': {'parent': "", 'vars': []}}
commands = []
n = input("Enter number: ")
for i in range(int(n)):
    command = input("Enter command: ")
    commands.append(command.split())
#print(commands)
for command in commands:
    if command[0] == "add":
        #print(command)
        add(command[1:])
    elif command[0] == "create":
        #print(command)
        create(command[1:])
    elif command[0] == "get":
        #print(command)
        get(command[1:])

print(spaces)