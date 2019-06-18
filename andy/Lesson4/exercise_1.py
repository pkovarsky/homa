"""Implement your own _unique function.
  First arg is collection.
  Function returns new collection of uniq items
  Usage of Set, Counter data structures is forbidden."""


def own_unique(collection):
    """
    Find unique elements at list and add them to new list.
    Unique element is the one that you can see only once
    :param collection: list for search unique elements
    :return: newList: new list with unique elements
    """
    if isinstance(collection, list):
        newlist = []
        for i in collection:
            if collection.count(i) == 1:
                newlist.append(i)
        print(newlist)
    else:
        print("Error: Invalid param type.Please enter list param.")


TESTLIST = ['1', '2', '3', 'a', 'b', 'c', 1, 2, 3, '3', 'c', 3]
INVALIDPARAM = "Invalid param"
own_unique(TESTLIST)
own_unique(INVALIDPARAM)
