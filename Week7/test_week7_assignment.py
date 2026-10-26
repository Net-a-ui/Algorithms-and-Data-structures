"""Behavior checks for the PA7 requirements; fixtures are test-only."""
import contextlib
import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import week7_assignment as app


def record(key):
    return (key, 'Country', '01/01/03', 'Employee', 'Shipping', 'Category',
            10.0, 2, 0.0, 1.0)


class AssignmentTests(unittest.TestCase):
    def invoke(self, function, answers, *args):
        with patch('builtins.input', side_effect=answers), contextlib.redirect_stdout(io.StringIO()):
            function(*args)

    def test_search_and_insertion_boundaries(self):
        self.assertEqual(app.binary_search([], '20'), (False, 0))
        table = [record('20'), record('40')]
        for key, expected in [('10', (False, 0)), ('20', (True, 0)),
                              ('30', (False, 1)), ('40', (True, 1)),
                              ('50', (False, 2))]:
            self.assertEqual(app.binary_search(table, key), expected)

    def test_add_validation_confirmation_and_duplicate(self):
        table = [record('20'), record('40')]
        values = ['30', 'C', 'D', 'E', 'S', 'Cat', 'bad', '12', 'bad', '3', '0', '1']
        self.invoke(app.add_using_key, values + ['N'], table)
        self.assertEqual(len(table), 2)
        self.invoke(app.add_using_key, values + ['Y'], table)
        self.assertEqual([r[0] for r in table], ['20', '30', '40'])
        self.assertIsInstance(table[1], tuple)
        self.assertEqual(table[1][6:8], (12.0, 3))
        self.invoke(app.add_using_key, ['30'], table)
        self.assertEqual(len(table), 3)

    def test_delete_found_missing_and_cancel(self):
        table = [record('20')]
        self.invoke(app.delete_using_key, [], table, '99')
        self.invoke(app.delete_using_key, ['N'], table, '20')
        self.assertEqual(len(table), 1)
        self.invoke(app.delete_using_key, ['Y'], table, '20')
        self.assertEqual(table, [])

    def test_update_each_field_preserves_key_and_other_fields(self):
        for index in range(1, 10):
            original = record('20')
            table = [original]
            value = '7' if index >= 6 else 'Changed'
            self.invoke(app.update_using_key, [chr(64 + index), value, 'Y'], table, '20')
            self.assertEqual(table[0][index], app.convert_field(index, value))
            self.assertEqual(table[0][:index], original[:index])
            self.assertEqual(table[0][index + 1:], original[index + 1:])
            self.assertIsInstance(table[0], tuple)

    def test_update_cancel_exit_missing_and_numeric_retry(self):
        table = [record('20')]
        original = table[:]
        self.invoke(app.update_using_key, ['J'], table, '20')
        self.invoke(app.update_using_key, [], table, '99')
        self.invoke(app.update_using_key, ['G', 'bad', '4', 'N'], table, '20')
        self.assertEqual(table, original)
        self.invoke(app.update_using_key, ['G', 'bad', '4', 'Y'], table, '20')
        self.assertEqual(table[0][7], 4)

    def test_loading_report_and_original_operations(self):
        table = app.load_data(app.ROOT / 'custsale.txt')
        self.assertEqual(len(table), 62)
        self.assertTrue(all(isinstance(r, tuple) for r in table))
        self.assertEqual(table, sorted(table, key=lambda r: r[0]))
        self.assertEqual(app.sum_quantity(table), sum(r[7] for r in table))
        self.assertEqual(table[app.find_largest_price(table)][6], max(r[6] for r in table))
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'report.txt'
            self.invoke(app.print_report, [], table, path)
            self.assertEqual(len(path.read_text().splitlines()), len(table) + 2)
            path.write_text('bad row\n')
            with self.assertRaises(ValueError):
                app.load_data(path)
            row = ' '.join(map(str, record('20'))) + '\n'
            path.write_text(row + row)
            with self.assertRaises(ValueError):
                app.load_data(path)
        self.invoke(app.delete_first_record, [], table)
        self.assertEqual(len(table), 61)
        self.assertEqual(app.find_largest_price([]), -1)

    def test_invalid_numbers(self):
        for value in ('nan', 'inf', '-inf', 'abc', ''):
            with self.assertRaises(ValueError):
                app.convert_field(6, value)
        with self.assertRaises(ValueError):
            app.convert_field(7, '1.5')

    def test_startup_failure_does_not_open_menu(self):
        with patch.object(app, 'load_data', side_effect=ValueError('bad data')):
            self.invoke(app.main, [])


if __name__ == '__main__':
    unittest.main()
