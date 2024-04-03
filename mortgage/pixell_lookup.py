"""
Description: Enumerations to keep track of valid mortgage rates 
and payment frequencies. A list to keep track of valid amortization periods.
Author: ACE Department
Edited By: {Student Name}
Date: {Date}
Usage: The enumerations and list in this file may be used when working 
with mortgages to ensure only valid rates, frequencies and amortization 
periods are used.
"""

from enum import Enum
from mortgage.pixell_lookup import MortgageRate, PaymentFrequency, VALID_AMORTIZATION
VALID_AMORTIZATION = {5, 10, 15, 20, 25, 30}

class MortgageRate(Enum):
    def __init__(loan_amount(float), rate(str), frequency(str), amortization(int)):
    

class PaymentFrequency(Enum):