'''
This program will read a data file sales record (custsale.txt) and load a list of
records (in memory) for processing...
'''

class SaleRecord:
    def __init__(self, data):
        self.order_num = data[0]
        self.country = data[1]
        self.date = data[2]
        self.employee = data[3]
        self.shipping = data[4]
        self.category = data[5]
        self.price = float(data[6])
        self.quantity = int(data[7])
        self.discount = float(data[8])
        self.freight = float(data[9])

    def get_order_num(self): return self.order_num
    def get_country(self): return self.country
    def get_price(self): return self.price
    def get_quantity(self): return self.quantity

    def get_data(self):
        return "%-8s %-12s %-10s %-10s %-18s %-15s %8.2f %6d %8.2f %8.2f" % (
        self.order_num, self.country, self.date, self.employee, self.shipping,
        self.category, self.price, self.quantity, self.discount, self.freight)

# 6.1 delete first record
def delete_first_record(table):
    if len(table) > 0:
        table.pop(0)
        print("First record deleted.")

# 6.2 sum quantity
def sum_quantity(table):
    total = 0
    for record in table:
        total += record.get_quantity()
    return total

# 6.3 find largest price
def find_largest_price(table):
    if len(table) == 0:
        return -1
    location = 0
    for index in range(len(table)):
        if table[index].get_price() > table[location].get_price():
            location = index
    return location

# 6.4 sort country A-Z
def sort_by_country(table):
    table.sort(key=lambda record: record.get_country())
    print("Records sorted by country.")

# 6.5 sort quantity high to low
def sort_by_quantity(table):
    table.sort(key=lambda record: record.get_quantity(), reverse=True)
    print("Records sorted by quantity.")

# 6.6 print report
def print_report(table, outfile):
    outfile.seek(0)
    outfile.truncate()
    outfile.write("CUSTOMER SALES REPORT".center(120) + "\n")
    outfile.write("Order    Country      Date       Employee   Shipping           Category           Price    Qty Discount  Freight\n")
    for record in table:
        outfile.write(record.get_data() + "\n")
    print("Report printed to report.txt")

# 6.7.1 find record using order number
def find_record_using_key(table, key):
    for index in range(len(table)):
        if table[index].get_order_num() == key:
            return index
    return -1

# 6.7.2 delete record at location
def delete_record_at_location(table, location):
    table.pop(location)

# 6.7 delete using primary key
def delete_using_key(table, key):
    location = find_record_using_key(table, key)
    if location == -1:
        print("Order number not found.")
        return
    display_records_on_screen([table[location]])
    answer = input("Delete this record? Y/N: ")
    if answer.upper() == "Y":
        delete_record_at_location(table, location)
        print("Record deleted.")

# 6.9 display records
def display_records_on_screen(table):
    print("\nCUSTOMER SALES RECORDS")
    print("Order    Country      Date       Employee   Shipping           Category           Price    Qty Discount  Freight")
    for record in table:
        print(record.get_data())

table = list()
infile = open("custsale.txt")
outfile = open("report.txt", "w")

for data in infile:
    table.append(SaleRecord(data.split()))

choice = ""
while choice.upper() != "Q":
    print("\n------------- MENU -------------")
    print("1. Delete first record")
    print("2. Sum quantity")
    print("3. Find largest price")
    print("4. Sort by country")
    print("5. Sort by quantity")
    print("6. Print report")
    print("7. Delete using Order number")
    print("9. Display records")
    print("Q. Quit")
    choice = input("Choose: ")

    if choice == "1":
        delete_first_record(table)
    elif choice == "2":
        print("Total Quantity Sold:", sum_quantity(table))
    elif choice == "3":
        location = find_largest_price(table)
        if location == -1:
            print("No records found.")
        else:
            display_records_on_screen([table[location]])
    elif choice == "4":
        sort_by_country(table)
    elif choice == "5":
        sort_by_quantity(table)
    elif choice == "6":
        print_report(table, outfile)
    elif choice == "7":
        delete_using_key(table, input("Order number to delete: "))
    elif choice == "9":
        display_records_on_screen(table)
    elif choice.upper() != "Q":
        print("Invalid choice.")

infile.close()
outfile.close()
