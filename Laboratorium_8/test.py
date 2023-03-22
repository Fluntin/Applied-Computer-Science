import unittest

from Syntaxfel import *


class SyntaxTest(unittest.TestCase):
    
    def testNumber(self):
        self.assertEqual(checkStructure("Cr0"), "För litet tal vid radslutet")
        self.assertEqual(checkStructure("Pb1"), "För litet tal vid radslutet")
        self.assertEqual(checkStructure("H01011"), "För litet tal vid radslutet 1011")
        self.assertEqual(checkStructure("Cr2"), "Formeln är syntatiskt korrekt")
        self.assertEqual(checkStructure("Cr1"), "För litet tal vid radslutet")

    def testLETTERletter(self):
        self.assertEqual(checkStructure("Cr"), "Formeln är syntatiskt korrekt")
        self.assertEqual(checkStructure("cr"), "Saknad stor bokstav vid radslutet cr")
    


if __name__ == '__main__':
    unittest.main()