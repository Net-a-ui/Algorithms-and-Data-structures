import time
import os

# Load the data file into a list of tuples.
def load_data(filename, limit):
    records = []
    file_path = os.path.join(os.path.dirname(__file__), filename)

    with open(file_path, "r", encoding="utf-8", errors="replace") as infile:
        for line in infile:
            line = line.rstrip("\n")

            if line:
                records.append(tuple(line.split("\t")))

            if limit is not None and len(records) >= limit:
                break

    return records


# Get the primary key used for sorting.
def get_key(record, data_type):
    if data_type == "1":
        return int(record[0])
    return record[0]


# Bubble Sort compares neighboring records.
def bubble_sort(records, data_type):
    for i in range(len(records)):
        swapped = False

        for j in range(len(records) - i - 1):
            if get_key(records[j], data_type) > get_key(records[j + 1], data_type):
                records[j], records[j + 1] = records[j + 1], records[j]
                swapped = True

        if not swapped:
            break


print("1 = Crime Data")
print("2 = Electric Vehicle Data")
data_type = input("Choose the data set: ")
filename = input("Enter the data file name: ")

sample_size = int(input("Number of records to load (0 = all): "))

if sample_size == 0:
    limit = None
else:
    limit = sample_size

records = load_data(filename, limit)

print("Records loaded:", len(records))

start_time = time.time()
bubble_sort(records, data_type)
end_time = time.time()

elapsed_time = end_time - start_time

print("Bubble Sort complete.")
print(f"Elapsed time: {elapsed_time:.4f} seconds")

print("\nFirst five sorted primary keys:")
for record in records[:5]:
    print(get_key(record, data_type))
