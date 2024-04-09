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
            raise ValueError("Loan amount must be positive.")
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
            raise ValueError("Amortization provided is invalid.")
        else:
            self.__amortization = amortization
        
    @property
    def loan_amount(self):
        """Accessor for loan_amount attribute"""
        return self.__loan_amount
    
    @loan_amount.setter
    def loan_amount(self, value):
        if value <= 0:
            raise ValueError("Loan amount must be positive.")
        self.__loan_amount = value

    @property
    def rate(self):
        """Accessor for rate attribute"""
        return self.__rate
    
    @rate.setter
    def rate(self, value):
        try:
            self.__rate = MortgageRate[value]
        except Exception as e:
            raise ValueError("Rate provided is invalid.")
        
    @property
    def frequency(self):
        """Accessor for frequency attribute"""
        return self.__frequency
    
    @frequency.setter
    def frequency(self, value):
        try: 
            self.__frequency = Mortgage[value]
        except Exception as e:
            raise ValueError("Frequency provided is invalid.")
        
    @property
    def amortization(self):
        """Accessor for amortization attribute"""
        return self.__amortization
    
    @amortization.setter
    def amortization(self, value):
        try:
            self.__amortization = Mortgage[value]
        except Exception as e:
            raise ValueError("Amortization provided is invalid.")
        
    def calculate_payment(self)->float:
        rate = self.__rate.value
        frequency = self.__frequency.value
        amortization = self.__amortization
        loan_amount = self.__loan_amount

        P = loan_amount
        n = amortization * frequency
        i = rate / frequency
        M = P * (i * (1 + i) ** n) / ((1 + i) ** n - 1)
        return M
    
    def __str__(self):
        rate = self.__rate.value * 100
        round(rate, 2)
        return (f"Mortgage Amount: ${self.loan_amount:,.2f} "
        f"Rate: {rate}% "
        f"Frequency: {self.frequency.name} "
        f"Amortization: {self.__amortization} "
        f"-- Calculated Payment: ${self.calculate_payment():,.2f} ")