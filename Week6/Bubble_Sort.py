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

# Enter a small number such as 50 to test.
# Enter 0 to use the complete dataset.
sample_size = int(input("Number of records to load (0 = all): "))

if sample_size == 0:
    limit = None
else:
    limit = sample_size

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

# Show the first five sorted primary keys.
print("\nFirst five sorted primary keys:")
for record in records[:5]:
    print(get_key(record, data_type))
