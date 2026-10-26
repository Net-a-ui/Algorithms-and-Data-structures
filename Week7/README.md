# Programming Assignment 7

Run `python week7_assignment.py` with Python 3. The program reads the included
`custsale.txt` beside the script. Option 3 creates `report.txt` there when requested.
Edits stay in memory; the input file is not changed.

## Source and requirements

Based on the uploaded **Programming Assignment 7.docx**, CPSC 34000, and the
Week1 program/data that the assignment explicitly requires upgrading.
The data file is an unchanged copy of `Week1/custsale.txt`.

- Load records as tuples; sort by primary key before opening the menu.
- Stop before the menu if loading, numeric conversion, or key uniqueness fails.
- Keep Week1's delete-first, sum-quantity, largest-price, report, key-delete,
  and display operations. Remove country and quantity sorting from the menu.
- Use binary search for key deletion, addition, and update.
- Confirm key deletion, insertion, and update before changing the list.
- Validate numeric entries and insert new records at their sorted position.
- Update one non-key field by constructing a new tuple at the same index;
  return to the main menu afterward, including when Exit is selected.

The main menu follows the document's example (8 quits), with quantity totals
at option 9 to preserve the Week1 operation. The update submenu contains all
nine non-key sales fields, with J to exit. The document's ITEM schema is an
example, not a replacement for the student's original data.

## Details not supplied by PA7

The document does not supply the actual sales schema, data file, numeric field
types, or report layout; these are taken from Week1. Order numbers remain
strings, as in Week1, and sort/search use the same string ordering. Price,
discount, and freight are floats; quantity is an integer.

PA7 does not specify numeric ranges, date validation rules, duplicate-key
handling, a required Python filename, submission packaging, or saving edits
back to the input file. This implementation rejects duplicate primary keys,
blank entries, and non-finite numbers, but invents no domain-specific numeric
ranges or date restrictions. It retains Week1's report layout and writes a
report only when requested. No generated report is included as assignment data.

## Verification

Run `python -m unittest discover -s Week7 -p "test_*.py"` from the repository root,
or `python -m unittest discover` from this folder.
