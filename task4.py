def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid number of arguments. Usage: add <name> <phone>"
    name, phone = args
    contacts[name] = phone
    return f"Contact '{name}' added with phone '{phone}'."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid number of arguments. Usage: change <name> <phone>"
    name, new_phone = args
    if name not in contacts:
        return f"Contact '{name}' not found."
    contacts[name] = new_phone
    return f"Contact '{name}' updated with phone '{new_phone}'."

def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid number of arguments. Usage: phone <name>"
    name = args[0]
    if name not in contacts:
        return f"Contact '{name}' not found."
    phone = contacts[name]
    return f"Phone number for '{name}' is '{phone}'."

def show_all(contacts):
    if not contacts:
        return "No contacts found."
    output = "Contacts:\n"
    for name, phone in contacts.items():
        output += f"{name}: {phone}\n"
    return output.strip()

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

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