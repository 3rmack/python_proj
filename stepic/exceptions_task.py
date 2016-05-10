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


def question_lst(q):
    ql = []
    for i in range(q):
        input_str = input()
        ql.append(input_str)
    return ql


def question(d, ql):
    answers = []
    for index in range(len(ql)):
        parents = set()
        parents_all = get_parents(d, ql[index], parents)
        # print("{0}: {1}".format(ql[index], parents_all))
        for called_earlier_class in ql[:index]:
            # print(question_str)
            # print(parents_all)
            if called_earlier_class in parents_all and ql[index] not in answers:
                answers.append(ql[index])
    return answers


def get_parents(d, child, parents):
    for parent in d[child]:
        parents.add(parent)
        try:
            for parent_parent in d[parent]:
                parents.add(parent_parent)
                get_parents(d, parent_parent, parents)
        except KeyError:
            continue
    return parents


def main():
    n = get_input()
    d = classes_dict(n)
    q = get_input()
    ql = question_lst(q)
    answers = question(d, ql)
    # print(d)
    # print(ql)
    # print(answers)
    for answer in answers:
        print(answer)


main()
