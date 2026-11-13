

TABLE_SIZE = 53

#hash function that sums the ASCII values of characters in the key and takes modulo TABLE_SIZE
def hash_function(key):
    total = 0
    for char in key:
        total += ord(char)
    return total % TABLE_SIZE
#load records from a file into the hash table
def load_records(filename):
    table = [[] for _ in range(TABLE_SIZE)]
    with open(filename, 'r') as file:
        #read each line from the file and insert it into the hash table
        for line in file:
            line = line.strip()
            if not line:
                continue
            #split the line into parts using tab as the delimiter
            parts = line.split("\t")
            if len(parts) != 7:
                continue
            #create a tuple from the parts to represent the record
            record = tuple(parts)
            index = hash_function(record[0])
            table[index].append(record)
    return table
#display a single record in a readable format
def display_record(record):
    print("\nRecord:")
    print("VIN:", record[0])
    print("City:", record[1])
    print("State:", record[2])
    print("Postal Code:", record[3])
    print("Model Year:", record[4])
    print("Make:", record[5])
    print("Model:", record[6])

#find a record in the hash table by VIN
def find_record(table, key):
    index = hash_function(key)
    #search for the record with the matching key in the corresponding bucket
    for record in table[index]:
        if record[0] == key:
            return index, record

    return index, None
#Function to add a new record to the hash table
def add_record(table):
    print("\n----- Add a New Record -----")
    vin = input("Enter VIN: ").strip()
    if not vin:
        print("VIN cannot be empty.")
        return

    #check if a record with the same VIN already exists
    index, existing = find_record(table, vin)
    if existing is not None:
        print("A record with this VIN already exists.")
        return
    #prompt the user for the remaining record details
    city = input("Enter City: ").strip()
    state = input("Enter State: ").strip()
    postal_code = input("Enter Postal Code: ").strip()
    model_year = input("Enter Model Year: ").strip()
    make = input("Enter Make: ").strip()
    model = input("Enter Model: ").strip()

    record = (vin, city, state, postal_code, model_year, make, model)
    print("\nNew record:")
    display_record(record)

    confirm = input("\nAdd this record? (y/n): ").strip().upper()
    #add the record to the hash table if the user confirms
    if confirm == "Y":
        table[index].append(record)
        print("Record added successfully.")
    else:
        print("Record not added.")

#Function to display the find record menu
def find_menu(table):
    print("\n----- Find a Record -----")
    #Prompt the user to enter the key (VIN) of the record to find
    key = input("Enter Record Key (VIN): ").strip()
    index, record = find_record(table, key)
    if record is None:
        print("Record not found.")
        return

    print("Record found at hash index:", index)
    display_record(record)
    record_menu(table, index, record)

#Function to delete a specific record from the hash table
def delete_record(table, index, record):
    print("\n----- Delete Record -----")
    display_record(record)
    confirm = input("\nDelete this record? (y/n): ").strip().upper()
    if confirm == "Y":
        table[index].remove(record)
        print("Record deleted successfully.")
    else:
        print("Record not deleted.")
#Function to update a specific record in the hash table
def update_record(table, index, record):
    while True:
        print("\n----- Update Record -----")
        print("G. City")
        print("H. State")
        print("I. Postal Code")
        print("J. Model Year")
        print("K. Make")
        print("L. Model")
        print("M. Return to main menu")

        choice = input("Select an option: ").strip().upper()

        if choice == "M":
            return
        #Map the user's choice to the corresponding field index and name
        field_map = {"G": 1, "H": 2, "I": 3, "J": 4, "K": 5, "L": 6}
        field_names = {
            1: "City",
            2: "State",
            3: "Postal Code",
            4: "Model Year",
            5: "Make",
            6: "Model"
        }
        #Check if the user's choice corresponds to a valid field
        if choice not in field_map:
            print("Invalid selection.")
            continue

        field_index = field_map[choice]
        new_value = input("Enter new " + field_names[field_index] + ": ").strip()

        updated = list(record)
        updated[field_index] = new_value
        updated = tuple(updated)

        print("\nUpdated record:")
        display_record(updated)
        #Display the updated record and ask for confirmation before saving
        confirm = input("\nSave this update? (Y/N): ").strip().upper()
        #ask for confirmation before saving the update
        if confirm == "Y":
            position = table[index].index(record)
            table[index][position] = updated
            print("Record updated successfully.")
        else:
            print("Update canceled.")

        return

#Function to display the record menu for a specific record
def record_menu(table, index, record):
    while True:
        print("\n------ Submenu ------")
        print("D. Delete Record")
        print("E. Update Record")
        print("F. Return to main menu")

        choice = input("Option: ").strip().upper()

        if choice == "D":
            delete_record(table, index, record)
            return
        elif choice == "E":
            update_record(table, index, record)
            return
        elif choice == "F":
            return
        else:
            print("Invalid selection.")

        #Submenu for record operations
def main():
    filename = "electric_car.txt"

    try:
        table = load_records(filename)
    except FileNotFoundError:
        print("Could not find electric_car.txt.")
        print("Place electric_car.txt in the same folder as this program.")
        return
    #Calculate the total number of records in the hash table
    total_records = sum(len(bucket) for bucket in table)

    print("Hash table loaded.")
    print("Records loaded:", total_records)
    print("Table size:", TABLE_SIZE)
    #Main menu loop begins here
    while True:
        print("\n-------- Main Menu --------")
        print("A. Add a New Record")
        print("B. Find a Record")
        print("C. Quit")

        choice = input("Option: ").strip().upper()

        if choice == "A":
            add_record(table)
        elif choice == "B":
            find_menu(table)
        elif choice == "C":
            print("Program ended.")
            break
        else:
            print("Invalid selection.")


if __name__ == "__main__":
    main()

