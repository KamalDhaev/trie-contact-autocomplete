from trie import Trie


def display_menu():
    print("\n===== MOBILE CONTACT SEARCH SYSTEM =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Autocomplete Suggestions")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")


def main():
    trie = Trie()

    # Sample contacts for demonstration
    sample_contacts = ["Arun", "Aravind", "Arjun", "Anu", "Rahul"]

    for contact in sample_contacts:
        trie.insert(contact)

    print("Welcome to Mobile Contact Search System!")

    while True:
        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = input("Enter contact name: ").strip()

            if not name:
                print("Contact name cannot be empty.")
            elif trie.search(name):
                print("Contact already exists.")
            else:
                trie.insert(name)
                print("Contact added successfully!")

        elif choice == "2":
            name = input("Enter contact name: ").strip()

            if not name:
                print("Please enter a contact name.")
            elif trie.search(name):
                print("Contact found!")
            else:
                print("Contact not found.")

        elif choice == "3":
            prefix = input("Enter prefix: ").strip()

            if not prefix:
                print("Please enter a prefix.")
            else:
                suggestions = trie.autocomplete(prefix)

                if suggestions:
                    print("Autocomplete suggestions:")
                    for name in suggestions:
                        print(name)
                else:
                    print("No matching contacts found.")

        elif choice == "4":
            name = input("Enter contact name to delete: ").strip()

            if trie.delete(name):
                print("Contact deleted successfully!")
            else:
                print("Contact not found.")

        elif choice == "5":
            contacts = trie.display_all()

            if contacts:
                print("All contacts:")
                for name in contacts:
                    print(name)
            else:
                print("No contacts available.")

        elif choice == "6":
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
