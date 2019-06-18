"""
Implement your own _map function.
  first arg is collection, second arg - callback (mapper)
  function returns new collection of mapped items.
  Usage of standard map functionality is forbidden.
"""


def own_map(collection: list, callback):
    """
    Implement your own _map function.
    :param collection: first arg is collection
    :param callback: second arg - callback (mapper)
    :return: function returns new collection of mapped items
    """
    newlist = []
    for i in collection:
        if isinstance(i, int):
            newlist.append(callback(i))
        else:
            print("gde zakladka?")
            exit()
    print(newlist)


def add_ten(value):
    """
    Plus ten func
    :param value: value
    :return: value plus 10
    """
    return value + 10


COLLECTION = [-10, 10, 20, 23, 123, 891, 999]
INVALIDCOLLECTION = [-10, 10, 20, 23, 123, "a", 999]
own_map(COLLECTION, add_ten)
own_map(INVALIDCOLLECTION, add_ten)
