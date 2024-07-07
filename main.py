from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
	pass

class Phone(Field):
    def __init__(self, value):
        if len(value) != 10:
            raise ValueError("Phone number must be 10 digits")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        
    def add_phone(self, phone):
        self.phones.append(Phone(phone))
        
    def remove_phone(self, phone):
        phone_to_remove = Phone(phone)
        if phone_to_remove in self.phones:
            self.phones.remove(Phone(phone))
    
    def edit_phone(self, old_phone, new_phone):
        try:
            index = self.phones.index(Phone(old_phone))
            self.phones[index] = Phone(new_phone)
        except ValueError:
            print("Phone not found")
    
    def find_phone(self, phone):
        phone_to_find = Phone(phone)
        return phone_to_find if phone_to_find in self.phones else None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def __str__(self):
        return '\n'.join(str(record) for record in self.data.values())
    
ab = AddressBook()
rec = Record("John Doe")
rec.add_phone("1234567890")
rec.add_phone("0987654321")
ab.add_record(rec)

print(ab)

rec.edit_phone("1234567890", "1112223333")
print(ab)



"""
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the arguments for the command."
        except KeyError:
            return "Contact not found."
        except Exception as e:
            return str(e)
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.lower().strip()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added"

@input_error
def change_contact(args, contacts):
    name, new_number = args
    contacts[name] = new_number
    return "Contact updated"

@input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts[name]
   
@input_error 
def show_all(args, contacts):
    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    return "No contacts are available."
    
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ").strip().lower()
        command, *args = parse_input(user_input)
        
        match command:
            case 'exit' | 'close':
                print('Good bye!')
                break
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, contacts))
            case "change": 
                print(change_contact(args, contacts))
            case "phone": 
                print(show_phone(args, contacts))
            case "all":
                print(show_all(args, contacts))
            case _:
                print("Invalid command")
    
if __name__ == "__main__":
    main()
"""