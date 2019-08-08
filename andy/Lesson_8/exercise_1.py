"""
- Implement PhoneBook class.
- Class should be an iterable.
- Class should contain methods:
  add_contact method (take object: IContact and add it to phone book)
  find_contact method (first match by name)
  remove_contact method (by name)
  call method (take object: IContact and print 'Calling to <contact name>...'])
  recent_calls property (returns recent calls<IContact>)
  add_to_favorites method (take object: IContact and add it to favorites (only if exists))
  favorites property (returns favorites contacts<IContact>)
- add_contact should check contact's number with regex(or other IValidator) before add it to phone book
- use OOP and SOLID
** IContact - Interface, PhoneBookContact - class
** IValidator - Interface, RegexValidator - class
** One validator per phone book instance
"""


class PhoneBook:

    recentCalls = []
    favoritesContacts = []

    def __init__(self):
        self.contacts = []

    def add_contact(self, firstname, lastname, phonenumber):
        self.contacts.append([firstname, lastname, phonenumber])

    def find_contact(self, firstname):
        for contact in self.contacts:
            if firstname in contact:
                return contact

    def remove_contact(self, firstname, lastname, phonenumber):
        for i in range(len(self.contacts)):
            if [firstname, lastname, phonenumber] == self.contacts[i]:
                self.contacts.pop(i)
                break

    def call_method(self, firstname):
        if self.find_contact(firstname):
            calling_contact = self.find_contact(firstname)
            print("Calling to ", calling_contact)
            self.recentCalls.append(calling_contact)
        else:
            print("Contact not found")

    @property
    def recent_calls(self):
        return self.recentCalls

    def add_to_favorites(self, firstname, lastname, phonenumber):
        if [firstname, lastname, phonenumber] in self.contacts:
            self.favoritesContacts.append([firstname, lastname, phonenumber])
        else:
            print("Contact not found")

    @property
    def favorites(self):
        return self.favoritesContacts


first = PhoneBook()
first.add_contact('petr', 'kovarsky', 102)
print("All contacts: ", first.contacts)
print("Found contact:", first.find_contact('petr'))
first.call_method('petr')
print("Recent calls: ", first.recent_calls)
first.add_to_favorites('petr', 'kovarsky', 102)
first.add_to_favorites('pizda', 'vagina', 103)
print("Favorites: ", first.favorites)

print("Added new contact =========================")
first.add_contact('petr', 'kovarsky', 108)
print("All contacts: ", first.contacts)
print("Found contact:", first.find_contact('petr'))
first.call_method(108)
print("Recent calls: ", first.recent_calls)
first.remove_contact('petr', 'kovarsky', 102)
print("All contacts after removing: ", first.contacts)
