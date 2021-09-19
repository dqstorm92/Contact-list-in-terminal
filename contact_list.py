#define a contact class, a contact has name, address, number phone and email
class Contact:
    def __init__(self, name, add, phone, email):
        self.name = name
        self.add = add
        self.phone = phone
        self.email = email

#Ask an user to enter information of a contact
def read_contact():
    name = input("Enter contact name: ")
    add = input("Enter contact address: ")
    phone = input("Enter contact number phone: ")
    email = input("Enter contact email: ")
    contact = Contact(name, add, phone, email)
    return contact

#Show information of a contact
def print_contact(contact):
    print("Name: " + contact.name)
    print("Address: " + contact.add)
    print("Number phone: " + contact.phone)
    print("Email: " + contact.email)

#Ask an user to enter information of all contacts, they first choose how many contacts are there
def read_contacts():
    contacts = []
    total = int(input("Enter how many contact: "))
    for i in range(total):
        print("Contact " + str(i+1) + ": ")
        con = read_contact()
        contacts.append(con)
    return contacts

#show information of all contact
def print_contacts(contacts):
    for i in range(len(contacts)):
        print("Contact ", str(i+1), ": ")
        print_contact(contacts[i])

#Write a contact to text file
def write_contact_to_txt(contact, file):
    file.write(contact.name + "\n")
    file.write(contact.add + "\n")
    file.write(contact.phone + "\n")
    file.write(contact.email + "\n")

#Write all contact to text file
def write_contacts_to_txt(contacts):
    total = len(contacts)
    with open("contact.txt", "w", encoding='utf-8') as file:
        file.write(str(total) + "\n")
        for i in range(total):
            write_contact_to_txt(contacts[i], file)

#Read a contact from txt
def read_contact_from_txt(file):
    name = file.readline().rstrip()
    add = file.readline().rstrip()
    phone = file.readline().rstrip()
    email = file.readline().rstrip()
    contact = Contact(name, add, phone, email)
    return contact

#Read all contact from txt
def read_contacts_from_txt():
    contacts = []
    with open("contact.txt", "r", encoding='utf-8') as file:
        total = file.readline()
        for i in range(int(total)):
            con = read_contact_from_txt(file)
            contacts.append(con)
    return contacts

#Menu contact list
def show_menu():
    print("************ Contact list *****************")
    print("| 1. Add new contact                      |")
    print("| 2. Show contact list                    |")
    print("| 3. Edit contact                         |")
    print("| 4. Delete contact                       |")
    print("| 5. Find contact with name               |")
    print("| 6. Exit and save                        |")
    print("*******************************************")


def select_in_range(prompt, min, max):
    choice = input(prompt)
    while not choice.isdigit() or int(choice) < min or int(choice) > max:
        choice = input(prompt)
    return int(choice)

def add_new_contact(contacts):
    print("Enter new contact information: ")
    total = int(input("Enter how many contact add? "))
    for i in range(total):
        print("New contact ", i+1, ": ")
        contact = read_contact()
        contacts.append(contact)
    return contacts

def edit_contact(contacts):
    total = len(contacts)
    while True:
        print("---------------- Edit contact ----------------")
        print("Contact list")
        print_contacts(contacts)
        print("----------------------------------------------")
        choice = select_in_range("Select a contact need edit: ", 1, total)
        while True:
            print("Edit contact ", choice, ": ")
            print("1. Name")
            print("2. Address")
            print("3. Number phone")
            print("4. Email")
            print("5. Exit edit contact")
            choi = select_in_range("Enter what you want to edit: ", 1, 5)
            if choi == 1:
                contacts[choice-1].name = input("Enter new contact name: ")
                print("Edited successfully")
            elif choi == 2:
                contacts[choice-1].add = input("Enter new contact address: ")
                print("Edited successfully")
            elif choi == 3:
                contacts[choice-1].phone = input("Enter new contact number phone: ")
                print("Edited successfully")
            elif choi == 4:
                contacts[choice-1].email = input("Enter new contact email: ")
                print("Edited successfully")
            elif choi == 5:
                print("Updated successfully!")
                break
        break
    return contacts

def delete_contact(contacts):
    print("Contact list: ")
    print_contacts(contacts)
    print("----------------------------------------")
    choice = select_in_range("Enter contact what you want to delete or enter '0' to exit: ", 0, len(contacts))
    if choice == 0:
        return contacts
    del contacts[choice-1]
    print("Deleted successfully!")
    return contacts

def find_contact_with_name(contacts):
    find_name = []
    total = len(contacts)
    name_find = input("Enter name need find? ")
    for i in range(total):
        if name_find.lower() in contacts[i].name.lower():
            find_name.append(contacts[i])
    if len(find_name) == 0:
        print("None")
    else:
        print("Contact list with name was found: ")
        print_contacts(find_name)
        choice = select_in_range("Enter contact you choose: ", 1, len(find_name))
        print("--------------------------------------")
        print("Contact you need: ")
        print_contact(find_name[choice-1])

def main():
    # contacts = read_contacts()
    # write_contacts_to_txt(contacts)
    # contacts = read_contacts_from_txt()
    # print_contacts(contacts)
    try:
        contacts = read_contacts_from_txt()
        print("Loaded date successfully!!")
    except:
        print("Welcome first user!!!")
    while True:
        show_menu()
        choice = select_in_range("Select an option (1-6): ", 1, 6)
        if choice == 1:
            add_new_contact(contacts)
            input("Press Enter to continute.")
        elif choice == 2:
            print_contacts(contacts)
            input("Press Enter to continute.")
        elif choice == 3:
            edit_contact(contacts)
            input("Press Enter to continute.")
        elif choice == 4:
            delete_contact(contacts)
            input("Press Enter to continute.")
        elif choice == 5:
            find_contact_with_name(contacts)
            input("Press Enter to continute.")
        elif choice == 6:
            write_contacts_to_txt(contacts)
            print("Saved successfully!")
            break
        else:
            print("Wrong input, Exist")
            break




main()