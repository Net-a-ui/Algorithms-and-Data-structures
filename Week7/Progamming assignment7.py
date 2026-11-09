# Week 7 Programming Assignment 7
# Records are stored as tuples in a list.

import os


# Load records from the data file into a list of tuples
def load_records(filename):
    records = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.rstrip("\n")

            if line:
                fields = line.split("\t")

                if len(fields) >= 6:
                    record = (
                        fields[0],
                        fields[1],
                        fields[2],
                        fields[3],
                        fields[4],
                        fields[5]
                    )
                    records.append(record)

    return records


# Sort records by the primary key
def sort_records(records):
    records.sort(key=lambda record: int(record[0]))


# Binary search for the primary key
def binary_search(records, key):
    key = int(key)
    low = 0
    high = len(records) - 1

    while low <= high:
        mid = (low + high) // 2
        middle_key = int(records[mid][0])

        if middle_key == key:
            return mid
        elif middle_key < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Binary search for the correct place to insert a new record
def find_insert_position(records, key):
    key = int(key)
    low = 0
    high = len(records)

    while low < high:
        mid = (low + high) // 2

        if int(records[mid][0]) < key:
            low = mid + 1
        else:
            high = mid

    return low


# Display one record
def display_one_record(record):
    print("Order Number:", record[0])
    print("Description:", record[1])
    print("On Hand:", record[2])
    print("Category:", record[3])
    print("Storehouse:", record[4])
    print("Price:", record[5])


# Delete the first record
def delete_first_record(records):
    if not records:
        print("No records.")
        return

    print("\nFirst record:")
    display_one_record(records[0])

    confirm = input("Confirm delete? (Y/N): ").upper()

    if confirm == "Y":
        records.pop(0)
        print("First record deleted.")
    else:
        print("Delete canceled.")


# Display the record with the largest price
def largest_value(records):
    if not records:
        print("No records.")
        return

    largest = records[0]

    for record in records:
        if float(record[0]) > float(largest[0]):
            largest = record

    print("\nRecord with the largest price:")
    display_one_record(largest)


# Print all records to a report file
def print_report(records):
    report_path = os.path.join(os.path.dirname(__file__), "report.txt")

    with open(report_path, "w", encoding="utf-8") as file:
        for record in records:
            file.write("\t".join(record) + "\n")

    print("Report created: report.txt")


# Delete a record using its primary key
def delete_record(records):
    key = input("Enter order number to delete: ").strip()

    if not key.isdigit():
        print("Order number must be a number.")
        return

    position = binary_search(records, key)

    if position == -1:
        print("Record not found.")
        return

    print("\nRecord found:")
    display_one_record(records[position])

    confirm = input("Confirm delete? (Y/N): ").upper()

    if confirm == "Y":
        records.pop(position)
        print("Record deleted.")
    else:
        print("Delete canceled.")


# Add a new record using its primary key
def add_record(records):
    order_num = input("Enter order number: ").strip()

    if not order_num.isdigit():
        print("Order number must be a number.")
        return

    order_num = str(int(order_num))

    if binary_search(records, order_num) != -1:
        print("Record already exists.")
        return

    description = input("Enter description: ")

    on_hand = input("Enter quantity on hand: ").strip()

    try:
        int(on_hand)
    except ValueError:
        print("Quantity must be a whole number.")
        return

    category = input("Enter category: ")
    storehouse = input("Enter storehouse: ")

    price = input("Enter price: ").strip()

    try:
        float(price)
    except ValueError:
        print("Price must be a number.")
        return

    new_record = (
        order_num,
        description,
        on_hand,
        category,
        storehouse,
        price
    )

    print("\nNew record:")
    display_one_record(new_record)

    confirm = input("Confirm adding this record? (Y/N): ").upper()

    if confirm == "Y":
        position = find_insert_position(records, order_num)
        records.insert(position, new_record)
        print("Record added.")
    else:
        print("Add canceled.")


# Update one field using the binary-search result
def update_record(records):
    key = input("Enter order number to update: ").strip()

    if not key.isdigit():
        print("Order number must be a number.")
        return

    position = binary_search(records, key)

    if position == -1:
        print("Record not found.")
        return

    old_record = records[position]

    print("\nRecord found:")
    display_one_record(old_record)

    print("\nUpdate Sub-Menu:")
    print("A. Description")
    print("B. OnHand")
    print("C. Category")
    print("D. Storehouse")
    print("E. Price")
    print("F. Exit")

    choice = input("Select the field option to make an update: ").upper()

    if choice == "F":
        print("Update canceled.")
        return

    updated_record = list(old_record)

    if choice == "A":
        updated_record[1] = input("Enter new description: ")

    elif choice == "B":
        new_value = input("Enter new OnHand: ").strip()

        try:
            int(new_value)
        except ValueError:
            print("OnHand must be a whole number.")
            return

        updated_record[2] = new_value

    elif choice == "C":
        updated_record[3] = input("Enter new category: ")

    elif choice == "D":
        updated_record[4] = input("Enter new storehouse: ")

    elif choice == "E":
        new_value = input("Enter new price: ").strip()

        try:
            float(new_value)
        except ValueError:
            print("Price must be a number.")
            return

        updated_record[5] = new_value

    else:
        print("Invalid choice.")
        return

    # Convert the changed list back into a tuple
    updated_record = tuple(updated_record)

    print("\nOld record:")
    display_one_record(old_record)

    print("\nNew record:")
    display_one_record(updated_record)

    confirm = input("Confirm update? (Y/N): ").upper()

    if confirm == "Y":
        records[position] = updated_record
        print("Record updated.")
    else:
        print("Update canceled.")


# Display all records
def display_records(records):
    if not records:
        print("No records.")
        return

    for record in records:
        display_one_record(record)
        print()


# Load the data file located in the same folder as this program
data_path = os.path.join(os.path.dirname(__file__), "custsale.txt")
records = load_records(data_path)

print("Records loaded:", len(records))

# Sort before using binary search
sort_records(records)


# Main Menu
while True:
    print("\nMAIN MENU")
    print("1. Delete First Record")
    print("2. Display the Record with a given Largest Value")
    print("3. Print all Records in a Report File")
    print("4. Delete a Record Using Key")
    print("5. Add a New Record Using Key")
    print("6. Update a Record Using Key")
    print("7. Display all Records on the Screen")
    print("8. Quit")

    choice = input("\nSelect the option number to process: ").strip()

    if choice == "1":
        delete_first_record(records)

    elif choice == "2":
        largest_value(records)

    elif choice == "3":
        print_report(records)

    elif choice == "4":
        delete_record(records)

    elif choice == "5":
        add_record(records)

    elif choice == "6":
        update_record(records)

    elif choice == "7":
        display_records(records)

    elif choice == "8":
        print("Goodbye.")
        break

    else:
        print("Invalid option. Please choose 1-8.")
