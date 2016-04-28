with open("dataset_24465_4.txt") as file_open, open("result.txt", "w") as file_write:
    text = file_open.read().splitlines()
    # print(text.splitlines())
    # print(repr(text))
    for line in text[::-1]:
        file_write.write(line)
        file_write.write("\n")
