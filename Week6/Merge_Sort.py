import time

# Load the data file into a list of tuples.
def load_data(filename, limit):
    records = []

    with open(filename, "r", encoding="utf-8", errors="replace") as infile:
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

# Enter a small number such as 50 to test.
# Enter 0 to use the complete dataset.
sample_size = int(input("Number of records to load (0 = all): "))

if sample_size == 0:
    limit = None
else:
    limit = sample_size

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

# Show the first five sorted primary keys.
print("\nFirst five sorted primary keys:")
for record in records[:5]:
    print(get_key(record, data_type))
