"""
Autor: Radek Kratochvíl and Petr Slavík
"""
import unittest
from CetnostZnaku import *


class TestCases(unittest.TestCase):

    def test_PocetZnak(self):                   ###    test počtu znaků ve vstupním textu, kdy povinný atribut #(hash) není brán jako znak    ###

        vstup = "AAAAAAAA#"
        self.assertEqual(PocetZnak(vstup), 8)


    def test_PocetZnak(self):                   ###    test počtu znaků ve vstupním souboru, kdy povinný atribut #(hash) není brán jako znak    ###

        vstup = "test_file.txt"
        self.assertEqual(PocetZnak(vstup),0)




    def test_MinZnak(self):
    
        vstup = "Python ma jen jednou X Y Z a mozna jeste nejaka dalsi pismena #"         

        self.assertEqual(MinZnak(vstup), ['H', 'U', 'X', 'K', 'L', '#'])



    def test_MinZnakNoHash(self):

        vstup = ""

        self.assertEqual(MinZnak(vstup), 0)



    def test_MaxZnakText(self):

        vstup = "Python ma spustu AAAAAAA#"

        self.assertEqual(MaxZnak(vstup), ['A'])

    
    
    
    def test_MaxZnakFile(self):
    
        vstup = "test_fileMax.txt"

        self.assertEqual(MaxZnak(vstup), ['A'])

    

    def test_MinZnakNoHashinFile(self):
    
        vstup = "test_file.txt"

        self.assertEqual(MinZnak(vstup),0)




if __name__ == '__main__':

    unittest.main()    