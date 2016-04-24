def get_input():
    n = int(input())
    return n


def classes_dict(n):
    d = dict()
    for i in range(n):
        input_str = input()
        class_list = input_str.split()
        for item in class_list:
            if item != ":" and item not in d:
                d[item] = []
        for parent in class_list[2:]:
            d[class_list[0]].append(parent)
    return d


def question(d, q):
    answers = []
    for i in range(q):
        input_str = input()
        question_list = input_str.split()
        parents = []
        parents_all = get_parents(d, question_list[1], parents)
        # print(parents_all)
        # answer = check(d, question_list[0], question_list[1])
        # answers.append(answer)
        if question_list[0] in parents_all or question_list[0] == question_list[1]:
            answers.append("Yes")
        else:
            answers.append("No")
    return answers


def get_parents(d, child, parents):
    for parent in d[child]:
        parents.append(parent)
        try:
            for parent_parent in d[parent]:
                parents.append(parent_parent)
                get_parents(d, parent_parent, parents)
        except KeyError:
            continue
    return parents


# def check(d, parent, child):
    # try:
    #     answer = "No"
    #     if parent == child or parent in d[child]:
    #         answer = "Yes"
    #     # elif parent in d[child]:
    #     #     # print("{0} {1}".format(parent, d[child]))
    #     #     answer = "Yes"
    #     else:
    #         for p in d[child]:
    #             answer = check(d, parent, p)
    #     return answer
    # except KeyError:
    #     #answers.append("No")
    #     answer = "No"
    #     return answer


def main():
    n = get_input()
    d = classes_dict(n)
    #print(d)
    q = get_input()
    answers = question(d, q)
    #print(answers)
    # print(d["classD"])
    # print(d["classG"])
    # print(d["classF"])
    # print(d["classH"])
    for answer in answers:
        print(answer)


main()
