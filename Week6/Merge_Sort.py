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


# Merge two sorted lists.
def merge(left, right, data_type):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if get_key(left[i], data_type) <= get_key(right[j], data_type):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Merge Sort divides, sorts, and merges the records.
def merge_sort(records, data_type):
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

sample_size = int(input("Number of records to load (0 = all): "))

if sample_size == 0:
    limit = None
else:
    limit = sample_size

records = load_data(filename, limit)

print("Records loaded:", len(records))

start_time = time.time()
records = merge_sort(records, data_type)
end_time = time.time()

elapsed_time = end_time - start_time

print("Merge Sort complete.")
print(f"Elapsed time: {elapsed_time:.4f} seconds")

print("\nFirst five sorted primary keys:")
for record in records[:5]:
    print(get_key(record, data_type))
