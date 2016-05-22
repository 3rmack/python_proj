string = input("Enter string: ")
i = len(string)//2
print(string[i])
if string[0] == string[i]:
    new_string = string[1:i]
    print(new_string)
