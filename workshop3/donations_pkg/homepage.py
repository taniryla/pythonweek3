def atm_menu(name):
    while True:
        print(f"User: {name}")
        print("------------------------------------------")
        print("| 1.    Balance     | 2.    Deposit      |")
        print("------------------------------------------")
        print("------------------------------------------")
        print("| 3.    Withdraw    | 4.    Logout       |")
        print("------------------------------------------")
        option = input("Choose an option:")
        if input == "1":
            account.show_balance(balance)
        elif input == "2":
            account.deposit(balance)
            print(f"Current Balance: ${float(balance)}")
        elif input == "3":
            account.withdraw(balance)
            print(f"Current Balance: ${float(balance)}")
        else:
            account.logout(name)
            break