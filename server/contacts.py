import Contacts
from pprint import pprint

class ContactInfo:
    def add_info(self, contact, stop):
        # if contact.isKeyAvailable_(Contacts.CNContactEmailAddressesKey):
        #     print(", ".join(val.value() for val in contact.emailAddresses()))
        if contact.isKeyAvailable_(Contacts.CNContactPhoneNumbersKey):
            numbers = list(val.value().stringValue() for val in contact.phoneNumbers())
            for n in numbers:
                self.contacts[n] = (contact.givenName() + " " + contact.familyName()).strip()
        else:
            print("Contact without e-mail")

    def get(self):
        return self.contacts

    def __init__(self):
        self.contacts = {}
        # request access to contacts
        store = Contacts.CNContactStore.alloc().init()
        store.requestAccessForEntityType_completionHandler_(
            Contacts.CNEntityTypeContacts, lambda x, y: print('Requested access')
        )

        fetchRequest = Contacts.CNContactFetchRequest.alloc().initWithKeysToFetch_(
            [Contacts.CNContactEmailAddressesKey, Contacts.CNContactPhoneNumbersKey, Contacts.CNContactGivenNameKey, Contacts.CNContactFamilyNameKey]
        )

        store = Contacts.CNContactStore.alloc().init()
        ok, error = store.enumerateContactsWithFetchRequest_error_usingBlock_(
            fetchRequest, None, self.add_info
        )
        if not ok:
            print("Fetching contacts failed", error)

        pprint(self.contacts)


if __name__ == "__main__":
    ContactInfo()