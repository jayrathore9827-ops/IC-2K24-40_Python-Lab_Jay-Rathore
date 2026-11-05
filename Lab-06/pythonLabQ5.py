# Store contacts as name -> {"phones": [list of numbers], "email": ..., "city": ...}
directory = {}

def is_valid_phone(phone):
    """Helper function to check if phone is exactly 10 digits."""
    return phone.isdigit() and len(phone) == 10

def phone_exists_globally(phone, dir_dict):
    
    for data in dir_dict.values():
        if phone in data["phones"]:
            return True
    return False

def addContact():
    global directory
    name = str(input("Enter Contact Name: ")).strip()
    if not name:
        print("Name cannot be empty.")
        return
        
    if name in directory:
        print("Contact already exists! Use 'Add another number' option to append numbers.")
        return
        
    phone = str(input("Enter 10-digit Phone Number: ")).strip()
    if not is_valid_phone(phone):
        print("Rejected: Phone number must be exactly 10 digits.")
        return
        
    if phone_exists_globally(phone, directory):
        print("Rejected: This phone number already belongs to another contact.")
        return
        
    email = str(input("Enter Email: ")).strip()
    city = str(input("Enter City: ")).strip()
    
    directory[name] = {
        "phones": [phone],
        "email": email,
        "city": city
    }
    print(f"Contact '{name}' added successfully!")

def addAnotherNumber():
    global directory
    name = str(input("Enter existing contact name: ")).strip()
    if name not in directory:
        print("Contact not found!")
        return
        
    phone = str(input("Enter new 10-digit Phone Number to add: ")).strip()
    if not is_valid_phone(phone):
        print("Rejected: Phone number must be exactly 10 digits.")
        return
        
    if phone_exists_globally(phone, directory):
        print("Rejected: This phone number already belongs to another contact.")
        return
        
    if phone in directory[name]["phones"]:
        print("This contact already has this phone number.")
        return
        
    directory[name]["phones"].append(phone)
    print(f"Phone number added successfully to {name}.")

def updateContact():
    global directory
    name = str(input("Enter contact name to update: ")).strip()
    if name not in directory:
        print("Contact not found!")
        return
        
    print("What would you like to update?")
    print("1. Email")
    print("2. City")
    choice = input("Enter choice (1 or 2): ").strip()
    
    if choice == '1':
        new_email = str(input("Enter new email: ")).strip()
        directory[name]["email"] = new_email
        print("Email updated successfully!")
    elif choice == '2':
        new_city = str(input("Enter new city: ")).strip()
        directory[name]["city"] = new_city
        print("City updated successfully!")
    else:
        print("Invalid choice.")

def deleteContact():
    global directory
    name = str(input("Enter contact name to delete: ")).strip()
    deleted_record = directory.pop(name, None)
    if deleted_record is not None:
        print(f"Contact '{name}' deleted successfully.")
    else:
        print("Contact does not exist. No crash occurred.")

def searchContact():
    global directory
    if not directory:
        print("Directory is empty.")
        return
        
    query = str(input("Enter partial or full name to search: ")).strip().lower()
    found = False
    
    print("\n--- Search Results ---")
    for name, data in directory.items():
        if query in name.lower():
            print(f"Name: {name} | Phones: {data['phones']} | Email: {data['email']} | City: {data['city']}")
            found = True
            
    if not found:
        print("No matching contacts found.")

def showReports():
    global directory
    if not directory:
        print("Directory is empty.")
        return

    print("\n--- PHONE DIRECTORY REPORTS & UTILITIES ---")

    
    reverse_lookup = {phone: name for name, data in directory.items() for phone in data['phones']}
    
    print("\n1. Reverse Lookup:")
    search_num = str(input("Enter a phone number to look up owner: ")).strip()
    owner = reverse_lookup.get(search_num)
    if owner:
        print(f"   Number {search_num} belongs to: {owner}")
    else:
        print(f"   Number {search_num} not found in directory.")

    
    city_groups = {}
    for name, data in directory.items():
        city_groups.setdefault(data['city'], []).append(name)
        
    print("\n2. Contacts Grouped by City:")
    for city, names in city_groups.items():
        print(f"   {city} -> {names}")

    
    multi_number_contacts = [name for name, data in directory.items() if len(data['phones']) > 1]
    print("\n3. Contacts with More Than One Number:")
    if multi_number_contacts:
        for name in multi_number_contacts:
            print(f"   - {name} ({directory[name]['phones']})")
    else:
        print("   None")

    
    print("\n4. Full Directory (Alphabetical Order):")
    for name in sorted(directory.keys()):
        data = directory[name]
        print(f"   - {name}: Phones: {data['phones']} | Email: {data['email']} | City: {data['city']}")

while True:
    print("\n--- Phone Directory Menu ---")
    print("1. Add contact")
    print("2. Add another number to an existing contact")
    print("3. Update email or city")
    print("4. Delete contact")
    print("5. Search contact (Partial name)")
    print("6. Reports & Reverse Lookup")
    print("7. Exit")
    
    choice = input("Enter your choice (1-7): ").strip()
    
    if choice == '1':
        addContact()
    elif choice == '2':
        addAnotherNumber()
    elif choice == '3':
        updateContact()
    elif choice == '4':
        deleteContact()
    elif choice == '5':
        searchContact()
    elif choice == '6':
        showReports()
    elif choice == '7':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice! Please select between 1 and 7.")
