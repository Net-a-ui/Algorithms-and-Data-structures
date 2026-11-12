# Week 11 - Programming Assignment 9: Hash Table

Run from this folder with Python 3:

```powershell
python "Programming assignment9.py"
```

The program loads the 500 tab-separated records in `electric_car.txt` into a fixed-size hash table of 53 buckets. VIN is the key; collisions are stored as multiple tuples in a bucket.

Main menu: A adds a record, B finds a record by VIN, and C quits.
After finding a record: D deletes it, E opens the field-update menu, and F returns to the main menu.
The update menu supports City, State, Postal Code, Model Year, Make, and Model. M returns to the main menu. Updates change one field at a time and preserve the VIN.

Add, delete, and update operations request confirmation and provide feedback. Changes exist in memory for the current session; the original data file is not overwritten.

Validation: 27 checks passed for loading, hashed placement, collisions, lookup, add/delete confirmations and cancellations, all six update fields, invalid selections, menu navigation, and quitting.
