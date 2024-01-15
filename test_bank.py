import re

from savings_account import create_savings_account
from cd_account import create_cd_account

def search_file(file, pattern):
    content = open(file).read()
    if re.search(pattern, content, re.MULTILINE):
        return True
    return False


# Create the Savings Account Function (35 points)
def test_savings_account() :
    assert search_file("savings_account.py", rf"from Account import Account") == True, "The Account class from the Accounts.py file is imported. (4 points)"

    assert search_file("savings_account.py", rf"Account\(balance, 0\)") == True, "In the create_savings_account function, an instance of the Account class is created and the balance and interest parameters are passed to the Account class. (6 points)"

    assert search_file("savings_account.py", rf"interest_earned \= balance \* interest_rate \/ 100 \* months \/ 12") == True, "The interest earned is calculated and assigned to a variable. (4 points)"

    assert search_file("savings_account.py", rf"updated_balance \= balance \+ interest_earned") == True, "The savings account balance is updated by adding the interest earned to the balance and assigned to a variable. (4 points)"

    assert search_file("savings_account.py", rf"account\.set_balance\(updated_balance\)") == True, "The updated balance is passed to the set balance method using the instance of the Account class. (6 points)"

    assert search_file("savings_account.py", rf"account.set_interest\(interest_earned\)") == True, "The interest earned is passed to the set balance method using the instance of the Account class. (6 points)"

    assert create_savings_account(1000, 2, 24) == (1040, 40), "The updated balance and interest earned are returned by the function. (5 points)"


# Create the CD Account Function (35 points)
def test_cd_account() :
    assert search_file("cd_account.py", rf"from Account import Account") == True, "The Account class from the Accounts.py file is imported. (4 points)"

    assert search_file("cd_account.py", rf"Account\(balance, 0\)") == True, "In the create_cd_account function, an instance of the Account class is created and the balance and interest parameters are passed to the Account class. (6 points)"

    assert search_file("cd_account.py", rf"interest_earned \= balance \* interest_rate \/ 100 \* months \/ 12") == True, "The interest earned is calculated and assigned to a variable. (4 points)"

    assert search_file("cd_account.py", rf"updated_balance \= balance \+ interest_earned") == True, "The CD account balance is updated by adding the interest earned to the balance and assigned to a variable. (4 points)"

    assert search_file("cd_account.py", rf"account\.set_balance\(updated_balance\)") == True, "The updated balance is passed to the set balance method using the instance of the Account class. (6 points)"

    assert search_file("cd_account.py", rf"account.set_interest\(interest_earned\)") == True, "The interest earned is passed to the set balance method using the instance of the Account class. (6 points)"

    assert create_cd_account(1000, 2, 24) == (1040, 40), "The updated balance and interest earned are returned by the function. (5 points)"


# Create the Main Function (30 points)
def test_customer_banking(capsys):
    assert search_file("customer_banking.py", rf'savings_balance \= float\(input\("Savings balance\: "\)\)\n\s+savings_interest \= float\(input\("Interest rate\: "\)\)\n\s+savings_maturity \= float\(input\("Months\: "\)\)') == True, "The user is prompted to set the savings balance, interest rate, and months for the savings account. (8 points)"
        
    assert search_file("customer_banking.py", rf'print\(f"Interest earned: \${{interest_earned:.2f}}"\)\n\s+print\(f"Updated savings account balance: \${{updated_savings_balance:.2f}}"\)') == True, "Code is written to print out the interest earned and updated savings account balance with interest earned for the given months. The values are formatted to two decimal places and thousandths. (6 points)"

    assert search_file("customer_banking.py", rf'cd_balance \= float\(input\("CD balance\: "\)\)\n\s+cd_interest \= float\(input\("Interest rate\: "\)\)\n\s+cd_maturity \= float\(input\("Months\: "\)\)') == True, "The user is prompted to set the savings balance, interest rate, and months for the CD account. (8 points)"

    assert search_file("customer_banking.py", rf'print\(f"Interest earned: \${{interest_earned:.2f}}"\)\n\s+print\(f"Updated CD account balance: \${{updated_cd_balance:.2f}}"\)') == True, "Code is written to print out the interest earned and updated CD account balance with interest earned for the given months. The values are formatted to two decimal places and thousandths. (6 points)"

    assert search_file("customer_banking.py", rf'if __name__ == "__main__":\n\s+# Call the main function.\n\s+main\(\)') == True, "The main function is called to run the program. (2 points)"
