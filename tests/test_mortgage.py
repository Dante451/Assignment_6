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
        error_message = "Loan amount must be positive."

        #Act
        with self.assertRaises(ValueError) as context:
            Mortgage(-69.00, "FIXED_3", "BI_WEEKLY", 30) 

        #Assert
        self.assertEqual(str(context.exception), error_message)

    def test_init_invalid_rate_input(self):
        #Arrange
        error_message = "Rate provided is invalid."

        #Act 
        with self.assertRaises(ValueError) as context:
            Mortgage(2500, "not_valid", "BI_WEEKLY", 30)

        #Assert
        self.assertEqual(str(context.exception), error_message)

    def test_init_invalid_frequency_input(self):
        #Arrange
        error_message = "Frequency provided is invalid."
            
        #Act 
        with self.assertRaises(ValueError) as context:
            Mortgage(2500, "FIXED_3", "not_valid", 30)

        #Assert
        self.assertEqual(str(context.exception), error_message)

    def test_init_invalid_amortization_input(self):
        #Arrange
        error_message = "Amortization provided is invalid."

        #Act 
        with self.assertRaises(ValueError) as context:
            Mortgage(2500, "FIXED_3", "BI_WEEKLY", 69)

        #Assert
        self.assertEqual(str(context.exception), error_message)

    def test_init_correct_attributes(self):
        #Arrange
        correct_everything = Mortgage(2500, "FIXED_3", "BI_WEEKLY", 25)
        #Act
        #Assert
        self.assertEqual(correct_everything.loan_amount, 2500)
        self.assertEqual(correct_everything.rate, MortgageRate.FIXED_3)
        self.assertEqual(correct_everything.frequency, PaymentFrequency.BI_WEEKLY)
        self.assertEqual(correct_everything.amortization, 25)

    def test_loan_amount_negative(self):
        #Arrange
        error_message = "Loan amount must be positive."
        correct_mortgage = Mortgage(2500, "FIXED_3", "BI_WEEKLY", 25)

        #Act
        with self.assertRaises(ValueError) as context:
            correct_mortgage.loan_amount = -500

        #Assert
        self.assertEqual(str(context.exception), error_message)
            
    def test_loan_amount_zero(self):
        #Arrange
        error_message = "Loan amount must be positive."
        correct_mortgage = Mortgage(2500, "FIXED_3", "BI_WEEKLY", 25)

        #Act
        with self.assertRaises(ValueError) as context:
            correct_mortgage.loan_amount = 0

        #Assert
        self.assertEqual(str(context.exception), error_message)

    def test_loan_amount_positive(self):
        #Arrange
        correct_mortgage = Mortgage(2500, "FIXED_3", "BI_WEEKLY", 25)

        #Act

        #Assert
        self.assertEqual(correct_mortgage.loan_amount, 2500) 

    def test_rate_invalid(self):
        #Arrange
        error_message = "Rate provided is invalid."
        correct_rate = Mortgage(2500, "FIXED_3", "BI_WEEKLY", 25)

        #Act
        with self.assertRaises(ValueError) as context:
            correct_rate.rate = "not_valid"

        #Assert
        self.assertEqual(str(context.exception), error_message)

    def test_rate_valid(self):
        #Arrange
        correct_rate = Mortgage(2500, "FIXED_3", "BI_WEEKLY", 25)
        #Act

        #Assert
        self.assertEqual(correct_rate.rate, MortgageRate.FIXED_3)

    def test_frequency_invalid(self):
        #Arrange
        error_message = "Frequency provided is invalid."
        correct_frequency = Mortgage(2500, "FIXED_3", "BI_WEEKLY", 25)

        #Act
        with self.assertRaises(ValueError) as context:
            correct_frequency.frequency = "not_valid"

        #Assert
        self.assertEqual(str(context.exception), error_message)
    
    def test_frequency_valid(self):
        #Arrange
        correct_frequency = Mortgage(2500, "FIXED_3", "BI_WEEKLY", 25)

        #Act

        #Assert
        self.assertEqual(correct_frequency.frequency, PaymentFrequency.BI_WEEKLY)

    def test_amortization_invalid(self):
        #Arrange
        error_message = "Amortization provided is invalid."
        correct_amortization = Mortgage(2500, "FIXED_3", "BI_WEEKLY", 25)

        #Act
        with self.assertRaises(ValueError) as context:
            correct_amortization.amortization = "not_valid"

        #Assert
        self.assertEqual(str(context.exception), error_message)

    def test_amortization_valid(self):
        #Arrange
        correct_amortization = Mortgage(2500, "FIXED_3", "BI_WEEKLY", 25)

        #Act

        #Assert
        self.assertEqual(correct_amortization.amortization, 25)

    def test_calculate_payment_correct(self):
        #Arrange
        expected_value = 7.35
        mortgage = Mortgage(2500, "FIXED_3", "BI_WEEKLY", 25)

        #Act
        actual_value = mortgage.calculate_payment()

        #Assert
        self.assertAlmostEqual(expected_value, actual_value, places = 2)

    def test_monthly(self):
        #Arrange
        expected = "Mortgage Amount: $2,500.00 Rate: 5.89% Frequency: MONTHLY Amortization: 25 -- Calculated Payment: $15.94 "
        mortgage = Mortgage(2500, "FIXED_3", "MONTHLY", 25)

        #Act
        actual = str(mortgage)
        
        #Assert
        self.assertEqual(expected, actual)

    def test_biweekly(self):
        #Arrange
        expected = "Mortgage Amount: $2,500.00 Rate: 5.89% Frequency: BI_WEEKLY Amortization: 25 -- Calculated Payment: $7.35 "
        mortgage = Mortgage(2500, "FIXED_3", "BI_WEEKLY", 25)

        #Act
        actual = str(mortgage)

        #Assert
        self.assertEqual(expected, actual)

    def test_weekly(self):
        #Arrange
        expected = "Mortgage Amount: $2,500.00 Rate: 5.89% Frequency: WEEKLY Amortization: 25 -- Calculated Payment: $3.68 "
        mortgage = Mortgage(2500, "FIXED_3", "WEEKLY", 25)

        #Act
        actual = str(mortgage)

        #Assert
        self.assertEqual(expected, actual)

    def test_repr(self):
        #Arrange
        expected = ("(2500, 0.0589, 26, 25)")
        mortgage = Mortgage(2500, "FIXED_3", "BI_WEEKLY", 25)

        #Act
        actual = repr(mortgage)

        #Assert
        self.assertEqual(expected, actual)