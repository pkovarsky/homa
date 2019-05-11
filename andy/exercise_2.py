"""" Exercise 2 """
# test 1
# Create tuple with chars from a long string.
TEST_STRING = "PeterPidorButNoOnePaysAttention"
TUPLE_RESULT = tuple(TEST_STRING)
# Slice last 20 chars in reversed order beging from 5th (5th from end).
SLICED = TUPLE_RESULT[-5:- 20:-1]
# Create dictionary from sliced chars. Print sorted keys of this dictionary.
KEY_VALUE_TUPLE = dict(enumerate(SLICED))
print("Test 1")
print("Sorted keys: ", sorted(KEY_VALUE_TUPLE.keys()))

# test 2
# Create list of chars from a long string.
FIRST_LIST = list(TEST_STRING)
# create another string
NEW_STRING = "AndHomaPidorToo"
# Extend list by chars from another string.
FIRST_LIST.extend(list(NEW_STRING))
# Remove duplicated items form list.
FIRST_LIST = list(set(FIRST_LIST))
# Delete middle element using slice functionality (important).
print("Test 2")
print("Before removing: ", FIRST_LIST)
MIDDLE_ELEMENT = FIRST_LIST[len(FIRST_LIST) // 2:len(FIRST_LIST) // 2 + 1]
FIRST_LIST.remove(MIDDLE_ELEMENT[0])
print("After removing: ", FIRST_LIST)

# test 3
# Create set with any elements.
TEST_SET = {'Parallel', 'Magic', 'Power Slide', 'Suicide', 'Wheeling'}
# Create dictionary from this enumerated set.
DICT_SET = dict(enumerate(TEST_SET))
print("Test 3")
print("Created dict: ", DICT_SET)

# test 4
# Create "AddressBook" dictionary {}.
# key should be a tuple (<street_name>, <building_number>)
# building address, where the people leave   value should be a dictionary {}.
# (key - (<floor_number>, <flat_number>),
# value - list ['citizen 1', 'citizen 2'])
ADDRESS_BOOK = {("Gudanova str", 4): {
    (3, 41): ["Short Pidor", "Young Pidor", "Fat Homeless 1", "USA Homeless 2"]}}

# test 5
# Create two Sets with numbers and chars.
FIRST_SET = {1, 2, 3, 4, 'Nizhnik', 'Peter'}
SECOND_SET = {3, 4, 2, 'Homa', 'Peter', 'Nizhnik', 'Pidor'}
print("Test 5")
# Find intersection
print("Intersection:", FIRST_SET & SECOND_SET)
# Find union
print("Union: ", FIRST_SET | SECOND_SET)
# Find difference between them.
print("Difference 1:", FIRST_SET - SECOND_SET)
print("Difference 2:", SECOND_SET - FIRST_SET)
# Use difference_update to update one set by other.
SECOND_SET.difference_update(FIRST_SET)
print("Updated second set:", SECOND_SET)
