#N1
tuple1 = tuple("ABCDEFGHIJKLMNOPQRSTU")
sliced = tuple1[15::-1]
print(sliced)

dtuple = dict.fromkeys(sliced, 1)
stuple = sorted(dtuple)
print(dtuple)
print(stuple)

#N2
list1 = list("Yaebalsobakyionabylaneprotiv")
list2 = list("PoroshenkoluchshiyprezidentUkrainy")
list1.extend(list2)
sorted_list =list(set(list1))
len(sorted_list)
middle_element = len(sorted_list) // 2
del middle_element
print(sorted_list)

#N3
set1 = {1, 3, 'a', 4, 66, "", 'B', 5}
enumerated_dict = {}
for k, v in enumerate(set1):
    enumerated_dict[k] = v
print(enumerated_dict)

#N4
AddressBook = {('street_name', 'street_number') : {('floor_number', 'flat_number'): ('citizen1', 'citizen2')}}
print(AddressBook)

#N5
set2 = {2, 3, "a", "b", "w", 44, ""}
print(set1 | set2, set1 & set2, (set1 - set2, set2 - set1))
set2.difference_update(set1)
print(set2)


