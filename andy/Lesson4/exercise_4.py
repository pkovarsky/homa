"""
Implement your own _find function.
first arg is callback, second arg - collection.
function returns first item from collection for which callback
function call return true
Usage of standard filter function or yor own _filter is forbidden.
"""

from collections import deque


def own_find(callback, collection):
    """
    Implement your own find PIDOR'S function.
    :param callback: first arg is callback
    :param collection: second arg - collection.
    :return: function returns first item from collection for which callback
    function call return true
    """
    newlist = deque([], len(collection))
    for i in collection:
        if callback(i):
            newlist.appendleft(i)
    print(newlist)


def pidor_detector(pidorlist):
    """
    Verify that element is string
    :param pidorlist: list
    :return: True or False
    """
    return isinstance(pidorlist, str)


PIDORLIST = ["Homa", 228, "Petr", "Nizhnik", 322, "Smusyaooo"]
own_find(pidor_detector, PIDORLIST)
