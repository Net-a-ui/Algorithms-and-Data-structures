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


# Merge two sorted lists into one sorted list.
def merge(left, right, data_type):
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):

        # Compare the primary keys.
        if get_key(left[left_index], data_type) <= get_key(right[right_index], data_type):
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Add records left over from either list.
    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result


# Merge Sort divides the list into smaller lists,
# sorts them, and then merges them together.
def merge_sort(records, data_type):

    # A list with 0 or 1 record is already sorted.
    if len(records) <= 1:
        return records

    middle = len(records) // 2

    left = merge_sort(records[:middle], data_type)
    right = merge_sort(records[middle:], data_type)

    return merge(left, right, data_type)


print("1 = Crime Data")
print("2 = Electric Vehicle Data")
data_type = input("Choose the data set: ")

filename = input("Enter the data file name: ")

limit = get_record_limit()

records = load_data(filename, limit)

print("Records loaded:", len(records))

# Start the timer before calling Merge Sort.
start_time = time.time()

records = merge_sort(records, data_type)

# Stop the timer after Merge Sort returns.
end_time = time.time()

elapsed_time = end_time - start_time

print("Merge Sort complete.")
print(f"Elapsed time: {elapsed_time:.4f} seconds")

print("\nSorted records:")
display_records(records, data_type)
