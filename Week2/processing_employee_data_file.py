from CommissionWorker import CommissionWorker
from PieceWorker import PieceWorker

infile = open("employee.txt")
table = list()

for data in infile:
    data_field = data.split()

    if data_field[0] == "C":
        emp = CommissionWorker(int(data_field[1]), data_field[2], data_field[3],
                               float(data_field[4]), float(data_field[5]),
                               float(data_field[6]))
        table.append(emp)

    elif data_field[0] == "P":
        emp = PieceWorker(int(data_field[1]), data_field[2], data_field[3],
                          float(data_field[4]), int(data_field[5]))
        table.append(emp)

print()
print("Gross-pay salary report")
print()
print("%-18s %-6s %-15s %-15s %10s" %
      ("Employee Type", "ID", "First Name", "Last Name", "Weekly Pay"))
print("---------------------------------------------------------------------")

for employee in table:
    print(employee.earnings())

infile.close()
