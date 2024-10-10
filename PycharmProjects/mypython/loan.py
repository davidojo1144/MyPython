class Loan:
    def _init_(self, first_name, last_name):
            self.__name = first_name + ' ' + last_name
            self.__interest_rate = 0
            self.__loan_period = int
            self.__monthly_payment = 0.0

    def get_name(self):
            return self.__name

    def get_loan_amount(self):
            return self.__loan_amount

    def __set_loan_amount(self, loan_amount):
            if loan_amount < 2000 or loan_amount > 100_000:
                raise ValueError('Loan amount cannot be less than 2000 or greater than 100_000.')
            else:
                self.__loan_amount = loan_amount
                return self.__loan_amount

