class PositiveList(list):
    def append(self, p_object):
        if p_object <= 0:
            raise NonPositiveError
        else:
            super().append(p_object)


class NonPositiveError(Exception):
    pass


lst = PositiveList()
lst.append(1)
lst.append(2)
print(lst)
lst.append(0)
