import unittest

from Syntaxfel import *


class SyntaxTest(unittest.TestCase):

    def testLETTERletter(self):
        self.assertEqual(checkStructure("Cr"), "Formeln är syntatiskt korrekt")
        self.assertEqual(checkStructure("C"), "Formeln är syntatiskt korrekt")
        self.assertEqual(checkStructure("cr"), "Saknad stor bokstav")
    
    def testNumber(self):
        self.assertEqual(checkStructure("Cr2"), "Formeln är syntatiskt korrekt")
        self.assertEqual(checkStructure("Cr1"), "För litet tal")

if __name__ == '__main__':
    unittest.main()