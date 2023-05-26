import unittest
from io import StringIO
import sys

from A1 import main

class TestPaperTape(unittest.TestCase):

    def test_normal_case(self):
        input_data = "4\n1 2 0\n"
        expected_output = "1.0150517651282178\n"
        
        # Redirect stdout to capture program output
        captured_output = StringIO()
        sys.stdout = captured_output

        # Run the code
        sys.stdin = StringIO(input_data)
        main()
        sys.stdin = sys.__stdin__  # Reset stdin
        sys.stdout = sys.__stdout__  # Reset stdout

        # Compare the actual and expected output
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_edge_case(self):
        input_data = "4\n2 0 1\n"
        expected_output = "0.5946035575013605\n"
        
        # Redirect stdout to capture program output
        captured_output = StringIO()
        sys.stdout = captured_output

        # Run the code
        sys.stdin = StringIO(input_data)
        main()
        sys.stdin = sys.__stdin__  # Reset stdin
        sys.stdout = sys.__stdout__  # Reset stdout

        # Compare the actual and expected output
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_invalid_case(self):
        input_data = "5\n0 0 1 0\n"
        expected_output = "impossible\n"
        
        # Redirect stdout to capture program output
        captured_output = StringIO()
        sys.stdout = captured_output

        # Run the code
        sys.stdin = StringIO(input_data)
        main()
        sys.stdin = sys.__stdin__  # Reset stdin
        sys.stdout = sys.__stdout__  # Reset stdout

        # Compare the actual and expected output
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_floating_point_case(self):
        input_data = "5\n1.99 0 1 0\n"

        # Redirect stdout to capture program output
        captured_output = StringIO()
        sys.stdout = captured_output

        # Run the code and check for ValueError
        sys.stdin = StringIO(input_data)
        with self.assertRaises(ValueError) as context:
            main()
            self.assertEqual(str(context.exception), "invalid literal for int() with base 10: '1.99'")

        sys.stdin = sys.__stdin__  # Reset stdin
        sys.stdout = sys.__stdout__  # Reset stdout


    def test_alternating_paper_availability(self):
        input_data = "6\n1 0 2 0 8\n"
        expected_output = "2.624707087757796\n"
        
        # Redirect stdout to capture program output
        captured_output = StringIO()
        sys.stdout = captured_output

        # Run the code
        sys.stdin = StringIO(input_data)
        main()
        sys.stdin = sys.__stdin__  # Reset stdin
        sys.stdout = sys.__stdout__  # Reset stdout

        # Compare the actual and expected output
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
