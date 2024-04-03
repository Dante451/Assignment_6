"""
Description: A class meant to manage Mortgage options.
Author: {Student Name}
Date: {Date}
Usage: Create an instance of the Mortgage class to manage mortgage records and 
calculate payments.
"""
from mortgage.pixell_lookup import MortgageRate, PaymentFrequency, VALID_AMORTIZATION 

class Mortgage:
    def __init__(self, loan_amount: float, rate: str, frequency: str, amortization: int):

        if loan_amount <= 0:
            raise ValueError("Loan amount must be positive")
        else:
            self.__loan_amount = loan_amount

        try:
            self.__rate = MortgageRate[rate]
        except Exception as e:
            raise ValueError("Rate provided is invalid.")
    
        try:
            self.__frequency = PaymentFrequency[frequency]
        except Exception as e:
            raise ValueError("Frequency provided is invalid.")
    
        if amortization not in VALID_AMORTIZATION:
            raise ValueError("Amortization provided is invalid")
        else:
            self.__amortization = amortization
