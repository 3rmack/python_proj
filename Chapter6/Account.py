from datetime import datetime


class Transaction(object):

    def __init__(self, amount, date, currency='USD', usd_exchange=1.0, description=None):
        self.__amount = amount
        self.__date = datetime.strptime(date, '%d.%m.%Y %H.%M.%S')
        self.__currency = currency
        self.__usd_exchange = usd_exchange
        self.__description = description

    def __repr__(self):
        return "Transaction({0.amount!r}, {0.date!r}, {0.currency!r}, {0.usd_exchange!r}, {0.description!r})".format(self)

    def __str__(self):
        return "({0.amount!r}, {0.date!r}, {0.currency!r}, {0.usd_exchange!r}, {0.description!r})".format(self)

    @property
    def amount(self):
        return self.__amount

    @property
    def date(self):
        return self.__date.strftime('%d.%m.%Y %H.%M.%S')

    @property
    def currency(self):
        return self.__currency

    @property
    def usd_exchange(self):
        return self.__usd_exchange

    @property
    def description(self):
        return self.__description

    @property
    def usd(self):
        return self.__amount * self.__usd_exchange


a = Transaction(23, '22.03.2015  15.06.23', usd_exchange=0.7)
print(a, a.amount, a.date, a.usd)
print a

b = Transaction(41.2, '21.03.2016 12.54.12')
print b
