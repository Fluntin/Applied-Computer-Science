import unittest
from formelkoll import *

class SyntaxTest(unittest.TestCase):
    def sample_inp_1(self):
        "Testar för första input exemplet"
        self.assertEqual(readformel('Na'), 'Formeln är syntaktiskt korrekt')
        self.assertEqual(readformel('H2O'), 'Formeln är syntaktiskt korrekt')
        self.assertEqual(readformel('Si(C3(COOH)2)4(H20)7'), 'Formeln är syntaktiskt korrekt')
        self.assertEqual(readformel('Na332'), 'Formeln är syntaktiskt korrekt') 

    def sample_inp_2(self):
        "Testar för andra input exemplet    "
        self.assertEqual(readformel('C(Xx4)5'), 'Okänd atom vid radslutet 4)5')
        self.assertEqual(readformel('C(OH4)C'), 'Saknad siffra vid radslutet C')
        self.assertEqual(readformel('C(OH4C'), 'Saknad högerparentes vid radslutet')
        self.assertEqual(readformel('H2O)Fe'), 'Felaktig gruppstart vid radslutet )Fe')
        self.assertEqual(readformel('H0'), 'För litet tal vid radslutet')
        self.assertEqual(readformel('H1C'), 'För litet tal vid radslutet C')
        self.assertEqual(readformel('H02C'), 'För litet tal vid radslutet 2C')
        self.assertEqual(readformel('Nacl'), 'Saknad stor bokstav vid radslutet cl')
        self.assertEqual(readformel('a'), 'Saknad stor bokstav vid radslutet a')
        self.assertEqual(readformel('(Cl)2)3'), 'Felaktig gruppstart vid radslutet )3')
        self.assertEqual(readformel(')'), 'Felaktig gruppstart vid radslutet )')
        self.assertEqual(readformel('2'), 'Felaktig gruppstart vid  radslutet 2') 