import datetime
class Logger:
    @staticmethod
    def log(message):
        with open("transactions.log", "a") as log_file:
            log_file.write(f"{datetime.datetime.now()}: {message}\n")

class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

class DepositService:
    @staticmethod
    def execute(account, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        account.balance += amount
        Logger.log(f"Deposited {amount} into {account.account_number}")
        print(f"Sending email notification: {amount} deposited into account {account.account_number}.")
    
class WithdrawService:
    @staticmethod
    def execute(account, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > account.balance:
            raise ValueError("Insufficient funds.")
        account.balance -= amount
        Logger.log(f"Withdrew {amount} from {account.account_number}")
        print(f"Sending email notification: {amount} withdrawn from account {account.account_number}.")
    
class GenerateStatementService:
    @staticmethod
    def execute(account):
        statement = f"Statement for Account: {account.account_number}\nBalance: {account.balance}\n"
        Logger.log(f"Generated statement for {account.account_number}")
        print(statement)    

if __name__ == "__main__":
    account = BankAccount("123456789")
    DepositService.execute(account, 100)
    WithdrawService.execute(account, 50)
    GenerateStatementService.execute(account)