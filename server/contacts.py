import Contacts
from pprint import pprint
import re

def format_phone_number(phone_number):
    # Extract all digits from the phone number string
    digits = re.findall(r'\d', phone_number)

    # Check if the length of digits is exactly 10
    if len(digits) == 10:
        formatted_number = '+1' + ''.join(digits)
    # If length is more than 10, consider the first 1-3 digits as the country code
    elif len(digits) > 10:
        # Find the index where the country code ends and the 10-digit number begins
        idx = next(i for i, x in enumerate(digits[1:], start=1) if x not in ('0', '1'))  # usually, country code doesn't start with 0 or 1
        formatted_number = '+' + ''.join(digits[:idx]) + ''.join(digits[idx:idx+10])
    else:
        # Raise an error if the phone number doesn't have enough digits
        raise ValueError('Phone number should have at least 10 digits')

    return formatted_number

phone_numbers = ['(123) 456-7890', '+1-123-456-7890', '+44 (1234) 567890']
formatted_numbers = [format_phone_number(number) for number in phone_numbers]
print(formatted_numbers)


class ContactInfo:
    def add_info(self, contact, stop):
        # if contact.isKeyAvailable_(Contacts.CNContactEmailAddressesKey):
        #     print(", ".join(val.value() for val in contact.emailAddresses()))
        if contact.isKeyAvailable_(Contacts.CNContactPhoneNumbersKey):
            numbers = []

            for n in list(val.value().stringValue() for val in contact.phoneNumbers()):
                try:
                    numbers.append(format_phone_number(n))
                except ValueError:
                    print(f'Invalid phone number: {n}')

            for n in numbers:
                self.contacts[n] = {
                    'name': (contact.givenName() + " " + contact.familyName()).strip(),
                    'image': f'data:image/jpg;base64,{contact.imageData().base64Encoding()}' if contact.imageData() else None,
                }
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
            [
                Contacts.CNContactEmailAddressesKey,
                Contacts.CNContactPhoneNumbersKey,
                Contacts.CNContactGivenNameKey,
                Contacts.CNContactFamilyNameKey,
                Contacts.CNContactImageDataKey,
            ]
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