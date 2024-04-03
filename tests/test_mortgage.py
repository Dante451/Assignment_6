"""
Description: A class used to test the Mortgage class.
Author: {Student Name}
Date: {Date}
Usage: Use the tests encapsulated within this class to test the MortgagePayment class.
"""
#python -m unittest -v tests/test_mortgage.py 
from unittest import TestCase 
from mortgage.mortgage import Mortgage 
from mortgage.pixell_lookup import MortgageRate, PaymentFrequency

class MortgageTests(TestCase):
    def test_init_invalid_amount_input(self):
        #Arrange

        #Act / Assert
        with self.assertRaises(ValueError):
            Mortgage(-69.00, "FIXED_3", "BI_WEEKLY", 30) 

    def test_init_invalid_rate_input(self):
        #Arrange

        #Act / Asseert
        with self.assertRaises(ValueError):
            Mortgage(2500, "not_valid", "BI_WEEKLY", 30)

    def test_init_invalid_frequency_input(self):
        #Arrange
            
        #Act / Assert
        with self.assertRaises(ValueError):
            Mortgage(2500, "FIXED_3", "not_valid", 30)

    def test_init_invalid_amortization_input(self):
        #Arrange

        #Act / Assert
        with self.assertRaises(ValueError):
            Mortgage(2500, "FIXED_3", "BI_WEEKLY", 69)
    #def test_init_invalid_correct_attributes(self):
        #Arrange
        #Act
        #Assert

