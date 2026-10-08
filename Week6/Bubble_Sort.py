import time
from pathlib import Path

# Load the data file into a list of tuples.
def load_data(filename, limit):
    records = []
    file_path = Path(__file__).with_name(filename)

    with open(file_path, "r", encoding="utf-8", errors="replace") as infile:
        for line in infile:
            line = line.rstrip("\n")

            if line:
                records.append(tuple(line.split("\t")))

            # Stop early when testing a small sample.
            if limit is not None and len(records) == limit:
                break

    return records


# Get the value used as the primary key.
def get_key(record, data_type):
    if data_type == "1":
        # Crime primary key is DR_NO, which is a number.
        return int(record[0])

    # Electric Vehicle primary key is VIN(1-10), which is text.
    return record[0]


# Ask for a record count between 1 and 50.
def get_record_limit():
    while True:
        number = input("Number of records to load (1-50): ")

        if number.isdigit():
            number = int(number)

            if number >= 1 and number <= 50:
                return number

        print("Please enter a number from 1 to 50.")


def shorten(value, width):
    value = str(value)

    if len(value) > width:
        return value[:width - 3] + "..."

    return value


def print_row(values, widths):
    row = ""

    for i in range(len(values)):
        row = row + shorten(values[i], widths[i]).ljust(widths[i]) + "  "

    print(row)


def display_records(records, data_type):
    if data_type == "1":
        headings = ["#", "DR_NO", "DATE OCC", "AREA", "CRIME", "AGE", "SEX", "LOCATION"]
        widths = [4, 12, 12, 16, 34, 5, 5, 28]

        print_row(headings, widths)
        print("-" * sum(widths))

        for i in range(len(records)):
            record = records[i]
            values = [
                i + 1,
                record[0],
                record[2].split()[0],
                record[5],
                record[9],
                record[11],
                record[12],
                record[24]
            ]
            print_row(values, widths)

    else:
        headings = ["#", "VIN", "COUNTY", "CITY", "YEAR", "MAKE", "MODEL", "EV TYPE"]
        widths = [4, 12, 14, 16, 6, 12, 14, 32]

        print_row(headings, widths)
        print("-" * sum(widths))

        for i in range(len(records)):
            record = records[i]
            values = [
                i + 1,
                record[0],
                record[1],
                record[2],
                record[5],
                record[6],
                record[7],
                record[8]
            ]
            print_row(values, widths)


# Bubble Sort compares neighboring tuples.
def bubble_sort(records, data_type):

    for i in range(len(records)):
        swapped = False

        for j in range(0, len(records) - i - 1):

            # Swap the records when the primary keys are out of order.
            if get_key(records[j], data_type) > get_key(records[j + 1], data_type):
                records[j], records[j + 1] = records[j + 1], records[j]
                swapped = True

        # Stop early when the list is already sorted.
        if not swapped:
            break


print("1 = Crime Data")
print("2 = Electric Vehicle Data")
data_type = input("Choose the data set: ")

filename = input("Enter the data file name: ")

limit = get_record_limit()

records = load_data(filename, limit)

print("Records loaded:", len(records))

# Start the timer before calling Bubble Sort.
start_time = time.time()

bubble_sort(records, data_type)

# Stop the timer after Bubble Sort returns.
end_time = time.time()

elapsed_time = end_time - start_time

print("Bubble Sort complete.")
print(f"Elapsed time: {elapsed_time:.4f} seconds")

print("\nSorted records:")
display_records(records, data_type)
