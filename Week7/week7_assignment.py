"""PA7: Week1 customer sales operations using sorted tuples and binary search."""

import math
from pathlib import Path

FIELDS = ('Order number', 'Country', 'Date', 'Employee', 'Shipping',
          'Category', 'Price', 'Quantity', 'Discount', 'Freight')
TYPES = (str, str, str, str, str, str, float, int, float, float)
HEADER = ('Order    Country      Date       Employee   Shipping           '
          'Category           Price    Qty Discount  Freight')
ROOT = Path(__file__).resolve().parent


def convert_field(index, value):
    value = value.strip()
    if not value:
        raise ValueError('A value is required.')
    converted = TYPES[index](value)
    if isinstance(converted, float) and not math.isfinite(converted):
        raise ValueError('Enter a finite number.')
    return converted


def load_data(path):
    table = []
    with open(path, encoding='utf-8') as infile:
        for line_number, line in enumerate(infile, 1):
            if not line.strip():
                continue
            parts = line.split()
            if len(parts) != len(FIELDS):
                raise ValueError(f'Line {line_number}: expected 10 fields.')
            try:
                table.append(tuple(convert_field(i, value)
                                   for i, value in enumerate(parts)))
            except ValueError as error:
                raise ValueError(f'Line {line_number}: {error}') from error
    table.sort(key=lambda record: record[0])
    for index in range(1, len(table)):
        if table[index - 1][0] == table[index][0]:
            raise ValueError(f'Duplicate order number: {table[index][0]}')
    return table


def binary_search(table, key):
    """Return (found, index); when absent, index is the sorted insertion point."""
    low, high = 0, len(table)
    while low < high:
        middle = (low + high) // 2
        if table[middle][0] < key:
            low = middle + 1
        else:
            high = middle
    return low < len(table) and table[low][0] == key, low


def format_record(record):
    return ('%-8s %-12s %-10s %-10s %-18s %-15s %8.2f %6d %8.2f %8.2f'
            % record)


def display_records_on_screen(table):
    print('\nCUSTOMER SALES RECORDS\n' + HEADER)
    for record in table:
        print(format_record(record))
    if not table:
        print('No records found.')


def delete_first_record(table):
    if table:
        table.pop(0)
        print('First record deleted.')
    else:
        print('No records found.')


def sum_quantity(table):
    return sum(record[7] for record in table)


def find_largest_price(table):
    if not table:
        return -1
    return max(range(len(table)), key=lambda index: table[index][6])


def print_report(table, path):
    with open(path, 'w', encoding='utf-8') as outfile:
        outfile.write('CUSTOMER SALES REPORT'.center(120) + '\n' + HEADER + '\n')
        for record in table:
            outfile.write(format_record(record) + '\n')
    print(f'Report printed to {path}')


def read_field(index):
    while True:
        try:
            return convert_field(index, input(FIELDS[index] + ': '))
        except ValueError as error:
            print(f'Invalid value: {error}')


def confirm(action):
    while True:
        answer = input(action + '? Y/N: ').strip().upper()
        if answer in ('Y', 'N'):
            return answer == 'Y'
        print('Enter Y or N.')


def delete_using_key(table, key):
    found, index = binary_search(table, key)
    if not found:
        print('Order number not found.')
        return
    display_records_on_screen([table[index]])
    if confirm('Delete this record'):
        table.pop(index)
        print('Record deleted.')


def add_using_key(table):
    key = read_field(0)
    found, index = binary_search(table, key)
    if found:
        print('Order number already exists.')
        return
    record = (key,) + tuple(read_field(i) for i in range(1, len(FIELDS)))
    display_records_on_screen([record])
    if confirm('Add this record'):
        table.insert(index, record)
        print('Record added.')


def update_using_key(table, key):
    found, index = binary_search(table, key)
    if not found:
        print('Order number not found.')
        return
    display_records_on_screen([table[index]])
    print('Update Submenu (order number cannot be changed)')
    for field_index in range(1, len(FIELDS)):
        print(f'{chr(64 + field_index)}. {FIELDS[field_index]}')
    print('J. Exit')
    while True:
        choice = input('Select one field: ').strip().upper()
        if choice == 'J':
            return
        if len(choice) == 1 and 'A' <= choice <= 'I':
            break
        print('Choose A through J.')
    field_index = ord(choice) - 64
    value = read_field(field_index)
    previous = table[index]
    updated = previous[:field_index] + (value,) + previous[field_index + 1:]
    display_records_on_screen([updated])
    if confirm('Update this record'):
        table[index] = updated
        print('Record updated.')
    # Exactly one field per invocation; return to the main menu.


def main():
    try:
        table = load_data(ROOT / 'custsale.txt')
    except (OSError, ValueError) as error:
        print(f'Cannot start application: {error}')
        return
    while True:
        print('\n1. Delete first record\n2. Display record with largest price'
              '\n3. Print all records in report file\n4. Delete record using key'
              '\n5. Add new record using key\n6. Update record using key'
              '\n7. Display all records\n8. Quit\n9. Sum quantity')
        choice = input('Choose: ').strip()
        if choice == '8':
            return
        if choice == '1':
            delete_first_record(table)
        elif choice == '2':
            index = find_largest_price(table)
            display_records_on_screen([] if index == -1 else [table[index]])
        elif choice == '3':
            try:
                print_report(table, ROOT / 'report.txt')
            except OSError as error:
                print(f'Cannot write report: {error}')
        elif choice == '4':
            delete_using_key(table, read_field(0))
        elif choice == '5':
            add_using_key(table)
        elif choice == '6':
            update_using_key(table, read_field(0))
        elif choice == '7':
            display_records_on_screen(table)
        elif choice == '9':
            print('Total Quantity Sold:', sum_quantity(table))
        else:
            print('Invalid choice.')


if __name__ == '__main__':
    main()
