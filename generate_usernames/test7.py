import collections


username = "test_iser"
fields = ["test_forename", ]

User = collections.namedtuple("User", "USERNAME FORENAME MIDDLENAME SURNAME ID")
user = User(username, fields[FORENAME], fields[MIDDLENAME], fields[SURNAME], fields[ID])