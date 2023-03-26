import io
import sys
import unittest
from contextlib import redirect_stdout
from Backup import *

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

class SyntaxTest(unittest.TestCase):
    def test_inp_1(self):
        "Testar för första input exemplet"
        self.assertEqual(check_structure('Na'), 'Formeln är syntaktiskt korrekt')
        self.assertEqual(check_structure('H2O'), 'Formeln är syntaktiskt korrekt')
        self.assertEqual(check_structure('Si(C3(COOH)2)4(H20)7'), 'Formeln är syntaktiskt korrekt')
        self.assertEqual(check_structure('Na332'), 'Formeln är syntaktiskt korrekt') 

    def test_inp_2(self):
        "Testar för andra input exemplet    "
        self.assertEqual(check_structure('C(Xx4)5'), 'Okänd atom vid radslutet 4)5')
        self.assertEqual(check_structure('C(OH4)C'), 'Saknad siffra vid radslutet C')
        self.assertEqual(check_structure('C(OH4C'), 'Saknad högerparentes vid radslutet')
        self.assertEqual(check_structure('H2O)Fe'), 'Felaktig gruppstart vid radslutet )Fe')
        self.assertEqual(check_structure('H0'), 'För litet tal vid radslutet')
        self.assertEqual(check_structure('H1C'), 'För litet tal vid radslutet C')
        self.assertEqual(check_structure('H02C'), 'För litet tal vid radslutet 2C')
        self.assertEqual(check_structure('Nacl'), 'Saknad stor bokstav vid radslutet cl')
        self.assertEqual(check_structure('a'), 'Saknad stor bokstav vid radslutet a')
        self.assertEqual(check_structure('(Cl)2)3'), 'Felaktig gruppstart vid radslutet )3')
        self.assertEqual(check_structure(')'), 'Felaktig gruppstart vid radslutet )')
        self.assertEqual(check_structure('2'), 'Felaktig gruppstart vid radslutet 2') 
        
if __name__ == '__main__':
    unittest.main()
