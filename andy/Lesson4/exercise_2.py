"""Implement your own _filter function.
  first arg is callback, second arg - collection.
  function returns new collection of items for which callback function call
  return true
  Usage of standard filter function is forbidden."""


def own_filter(collection, callback):
    """
    function returns new collection of items for which callback function call
    :param collection: list for search unique elements
    :param callback: call back function
    :return:
    """
    if isinstance(collection, list):
        newlist = []
        for i in collection:
            if isinstance(i, int):
                if callback(i):
                    newlist.append(i)
            else:
                print("NOGA")
                exit()
        print(newlist)
    else:
        print("Sosality")


def even_numbers(number):
    """
    Return even numbers
    :param number: number
    :return: True if number is even
    """
    return number % 2 == 0


def odd_numbers(number):
    """
    Return even numbers
    :param number: number
    :return: True if number is odd
    """
    return number % 2 != 0


NUMBERSLIST = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
own_filter(NUMBERSLIST, even_numbers)
own_filter(NUMBERSLIST, odd_numbers)
NUMBERSLIST.append('PANIN')
own_filter(NUMBERSLIST, even_numbers)
own_filter(NUMBERSLIST, odd_numbers)
INVALIDFORMAT = "Pidor"
own_filter(INVALIDFORMAT, even_numbers)
own_filter(INVALIDFORMAT, odd_numbers)
