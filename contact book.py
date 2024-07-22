import OS

FILE NAME = "contacts.txt"

contact_book = [ ]

def load_contacts():

if os.path.exists (FILE_NAME):

with open (FILE_NAME, "r") as file:

for line in file:
name, phone, email line.strip().split('|')

contact_book.append({"name": name, "phone": phone, "email": email})

def save_contacts():


with open(FILE_NAME, "w") as file:

for contact in contact_book:

file.write(f"({contact['name']}|{contact['phone']}|{contact['email']}\n")

def add_contact():
name = input("Enter name: ")

phone = input("Enter phone number: ")

email = input("Enter email: ")

contact_book.append({"name": name, "phone": phone, "email": email))

save_contacts()

print("Contact added successfully!")


def view_contacts():

if not contact_book:

print("Contact book is empty.")

else:

for idx, contact in enumerate (contact_book, 1):

print(f"(idx). Name: (contact['name']}, Phone: (contact['phone']), Email: contact['email']}")


def search_contact():

search_name = input("Enter the name to search: ")

found_contacts = [contact for contact in contact_book if search_name.lower() in contact['name'].lower()]

if found_contacts:

for contact in found_contacts:
print(f"Name: (contact['name']}, Phone: {contact['phone']), Email: contact['email']}")


else:

print("Contact not found.")

def update_contact():
Search_name = input ("Enter the name of the contact to update:")

For contact in contact _book;

if contact['name'].lower( ').lower() == search_name.lower():


print(f"Current details: Name: contact['name']), Phone: {contact['phone']}, Email: contact['email']}")

 contact['name'] = input("Enter new name (leave blank to keep current): ") or contact['name'

contact['phone'] = input("Enter new phone number (leave blank to keep current): ") or contact['phone']

 contact['email'] = input("Enter new email (leave blank to keep current): ") or contact['email']

save_contacts() I

print("Contact updated successfully!")

return

print("Contact not found.")

def delete_contact():

search_name = input("Enter the name of the contact to delete: ")

for contact in contact_book:

if contact['name'].lower() == search_name.lower():
 contact_book.remove(contact)

save contacts()
print("Contact deleted successfully!")

return

print("Contact not found.")

def main_menu():

load_contacts()

while True:

print("\nContact Book Menu:")

print("1. Add Contact")

print("2. View Contact List")

print("3. Search Contact")

print("4. Update Contact")

print("5. Delete Contact")

print("6. Exit")

choice = input("Enter your choice: ")

if choice == '1':

add_contact()

elif choice == '2':

view_contacts()

elif choice == '3':
search_contact()

elif choice == '4': update_contact()

elif choice == '5': delete_contact()

elif choice == '6':

break

else:

print("Invalid choice. Please try again.")

if _name_ == "_main_":

main_menu()