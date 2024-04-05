# Import the create_cd_account and create_savings_account functions
from utilities.cd_account import create_cd_account
from utilities.savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = input("\nWhat is the starting balance? ")
    savings_interest = input("\nWhat is the interest rate? ")
    savings_maturity = input("\nHow many months are your terms? ")

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    for i in savings_maturity:
        print(" MONTH | Interest Earned | Balance")
        print(f"{i} :<7 | {interest_earned} | {updated_savings_balance}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = input("\nWhat is the cd contribution amount? ")
    cd_interest = input("\nWhat is the cd interest rate? ")
    cd_maturity = input("\nHow many months till cd maturity? ")

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    for i in cd_maturity:
        print(" MONTH | Interest Earned | Balance")
        print(f"{i} :<7 | {interest_earned} | {updated_cd_balance}")

if __name__ == "__main__":
    # Call the main function.
    main()