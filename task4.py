def input_command_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Input a valid command."

    return inner

@input_command_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact was not found"
        except IndexError:
            return "Give me contact name to return phone for, please."

    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args

    if name in contacts:
        return f"{name} contact is already saved"

    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args

    if name not in contacts:
        return f"{name} contact is not found"

    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts[name]

#Couldn't find any possible exceptions here, so no decorator
def show_all(contacts):
    result = ""
    for name, phone in contacts.items():
        result += f"{name} : {phone}\r\n"
    return result.strip()

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()




