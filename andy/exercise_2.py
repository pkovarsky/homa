"""" Exercise 2 """
# test 1
TEST_STRING = "PeterPidorButNoOnePaysAttention"
TUPLE_RESULT = tuple(TEST_STRING)
SLICED = TUPLE_RESULT[len(TUPLE_RESULT) - 4:len(TUPLE_RESULT) - 20:-1]
# convert tuple to tuple with key/value pairs
KEY_VALUE_TUPLE = tuple(SLICED[i: i + 2] for i in range(0, len(SLICED), 2))
# print sorted dict keys
print("Test 1")
print("Sorted keys: ", sorted(dict(KEY_VALUE_TUPLE).keys()))

# test 2
FIRST_LIST = list(TEST_STRING)
# create new string
NEW_STRING = "AndHomaPidorToo"
# add second list to first list
FIRST_LIST.extend(list(NEW_STRING))
FIRST_LIST = list(set(FIRST_LIST))
# search middle element and convert to int type
print("Test 2")
print("Before removing: ", FIRST_LIST)
MIDDLE_ELEMENT = FIRST_LIST[int(len(FIRST_LIST) / 2):int(len(FIRST_LIST) / 2 + 1)]
FIRST_LIST.remove(MIDDLE_ELEMENT[0])
print("After removing: ", FIRST_LIST)

# test 3
TEST_SET = {'Parallel', 'Magic', 'Power Slide', 'Suicide', 'Wheeling'}
DICT_SET = dict(enumerate(TEST_SET))
print("Test 3")
print("Created dict: ", DICT_SET)

# test 4
ADDRESS_BOOK = {("Gudanova str", 4): {
    (3, 41): ["Short Pidor", "Young Pidor", "Fat Homeless 1", "USA Homeless 2"]}}

# test 5
FIRST_SET = {1, 2, 3, 4, 'Nizhnik', 'Peter'}
SECOND_SET = {3, 4, 2, 'Homa', 'Peter', 'Nizhnik', 'Pidor'}
print("Test 5")
print("Intersection:", FIRST_SET & SECOND_SET)
print("Union: ", FIRST_SET | SECOND_SET)
print("Difference 1:", FIRST_SET - SECOND_SET)
print("Difference 2:", SECOND_SET - FIRST_SET)
SECOND_SET.difference_update(FIRST_SET)
print("Updated second set:", SECOND_SET)
