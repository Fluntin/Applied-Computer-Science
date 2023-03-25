import io
import sys
import unittest
from contextlib import redirect_stdout
from Formelkoll import check_structure

# Na                     Formeln är syntaktiskt korrekt
# H2O                    Formeln är syntaktiskt korrekt
# Si(C3(COOH)2)4(H2O)7   Formeln är syntaktiskt korrekt
# Na332                  Formeln är syntaktiskt korrekt
  
# C(Xx4)5                Okänd atom vid radslutet 4)5
# C(OH4)C                Saknad siffra vid radslutet C
# C(OH4C                 Saknad högerparentes vid radslutet
# H2O)Fe                 Felaktig gruppstart vid radslutet )Fe
  
# H0                     För litet tal vid radslutet
# H1C                    För litet tal vid radslutet C
# H02C                   För litet tal vid radslutet 2C
# Nacl                   Saknad stor bokstav vid radslutet cl
# a                      Saknad stor bokstav vid radslutet a
# (Cl)2)3                Felaktig gruppstart vid radslutet )3
# )                      Felaktig gruppstart vid radslutet )
# 2                      Felaktig gruppstart vid radslutet 2

class MyTest(unittest.TestCase):
    def test_check_structure(self):
        # Define the input string
        input_str = 'Na\nH2O\nSi(C3(COOH)2)4(H2O)7\nNa332\n#'

        # Split the input string into a list of molecules
        molecules = input_str.strip().split('\n')

        # Define the expected output for each molecule
        expected_output = [
            'Formeln är syntaktiskt korrekt',
            'Formeln är syntaktiskt korrekt',
            'Formeln är syntaktiskt korrekt',
            'Formeln är syntaktiskt korrekt',
        ]

        # Test each molecule
        for i, molecule in enumerate(molecules):
            # Redirect stdin to a file-like object containing the molecule
            sys.stdin = io.StringIO(molecule + '\n')

            # Capture the output
            output_str = io.StringIO()
            with redirect_stdout(output_str):
                check_structure(molecule)

            # Get the output as a string
            output_line = output_str.getvalue().strip()

            # Check that the output matches the expected output
            self.assertEqual(output_line, expected_output[i])

if __name__ == '__main__':
    unittest.main()