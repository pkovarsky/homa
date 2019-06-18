"""
Implement your own _find function.
first arg is callback, second arg - collection.
function returns first item from collection for which callback
function call return true
Usage of standard filter function or yor own _filter is forbidden.
"""


def own_find(callback, collection):
    """
    Implement your own find PIDOR'S function.
    :param callback: first arg is callback
    :param collection: second arg - collection.
    :return: function returns first item from collection for which callback
    function call return true
    """
    for i in collection:
        if callback(i):
            print(i)
            break


def pidor_detector(pidorlist):
    """
    Verify that element is string
    :param pidorlist: list
    :return: True or False
    """
    return isinstance(pidorlist, str)


PIDORLIST = [228, "Homa", "Petr", "Nizhnik", 322, "Smusyaooo"]
own_find(pidor_detector, PIDORLIST)
NOPIDORLIST = [228, 322, 666]
own_find(pidor_detector, NOPIDORLIST)
