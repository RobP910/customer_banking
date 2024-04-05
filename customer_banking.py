# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input("\nWhat is the starting balance? "))
    savings_interest = float(input("\nWhat is the interest rate? "))
    savings_maturity = int(input("\nHow many months before maturity? "))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(" MONTH | Interest Earned | Balance")
    print(f"{savings_maturity:>3}    | {interest_earned:>9}       | ${updated_savings_balance:<25}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input("\nWhat is the CD contribution amount? "))
    cd_interest = float(input("\nWhat is the CD interest rate? "))
    cd_maturity = int(input("\nHow many months for the CD to mature? "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(" MONTH | Interest Earned | Balance")
    print(f"{cd_maturity:>3}    | {interest_earned:>9}       | ${updated_cd_balance:<25}")

if __name__ == "__main__":
    # Call the main function.
    main()
