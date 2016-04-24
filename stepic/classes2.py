def get_input():
    n = int(input("N: "))
    return n


def classes_dict(n):
    d = dict()
    for i in range(n):
        input_str = input("input classes: ")
        class_list = input_str.split()
        parent_list = []
        for parent_class in class_list[2:]:
            parent_list.append(parent_class)
        d[class_list[0]] = parent_list
    return d


def question(d, q):
    #answ = []
    answers = []
    for i in range(q):
        input_str = input("input question: ")
        question_list = input_str.split()
        # answer = "No"
        answer = check(d, question_list[0], question_list[1], answers)
        print(answer)
        #answers.append(answer)
        # if answ == "Yes":
        #     answers.append("Yes")
        # else:
        #     answers.append("No")
    return answers


def check(d, parent, child, answers):
    # answer = "No"
    try:
        answer = "No"
        if parent in d[child]:
            # print("{0} {1}".format(parent, d[child]))
            # answers.append("Yes")
            answer = "Yes"
        else:
            for p in d[child]:
                answer = check(d, parent, p, answers)
        return answer
    except KeyError:
        # answers.append("No")
        answer = "No"
        return answer


def main():
    n = get_input()
    d = classes_dict(n)
    q = get_input()
    question(d, q)


main()
