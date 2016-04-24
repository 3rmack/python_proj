import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self, obj):
        super(LoggableList, self).append(obj)
        self.log(obj)


tst = Loggable()
tst.log("test message")

lst = LoggableList()
lst.append(1)
lst.append(2)
print(lst)