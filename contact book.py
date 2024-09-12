
class ContactBook:
    def __init__(self):
       
        self.contacts = {}

 
    def add_contact(self, name, phone, email):
        if name in self.contacts:
            print(f"Contact '{name}' already exists.")
        else:
            self.contacts[name] = {'Phone': phone, 'Email': email}
            print(f"Contact '{name}' added successfully.")

    
    def search_contact(self, name):
        if name in self.contacts:
            print(f"Name: {name}\nPhone: {self.contacts[name]['Phone']}\nEmail: {self.contacts[name]['Email']}")
        else:
            print(f"Contact '{name}' not found.")

   
    def view_contacts(self):
        if self.contacts:
            print("Contact List:")
            for name, info in self.contacts.items():
                print(f"\nName: {name}\nPhone: {info['Phone']}\nEmail: {info['Email']}")
        else:
            print("No contacts available.")

   
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")


def main():
    contact_book = ContactBook()
    
    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. View All Contacts")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            name = input("Enter Name: ")
            phone = input("Enter Phone: ")
            email = input("Enter Email: ")
            contact_book.add_contact(name, phone, email)
        
        elif choice == '2':
            name = input("Enter Name to Search: ")
            contact_book.search_contact(name)
        
        elif choice == '3':
            contact_book.view_contacts()
        
        elif choice == '4':
            name = input("Enter Name to Delete: ")
            contact_book.delete_contact(name)
        
        elif choice == '5':
            print("Exiting Contact Book...")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
