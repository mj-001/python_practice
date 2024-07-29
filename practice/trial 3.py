
balance=0


def deposit():
    global balance
    deposit_amount= int(input("How much do you wish to deposit?"))
    if deposit_amount <= 0:
        return print(f"Invalid input .Kindly enter number greater than zero")
    if deposit_amount > 0:
        balance += deposit_amount
        return print(f"You deposit was successfull .New balance is {balance}")



def withdrawal():
    global balance
    withdrawal_amount = int(input("How much do you wish to withdraw?"))
    if withdrawal_amount == 0 or withdrawal_amount>balance:
        return print(f"Invalid input. Kindly input number greater than your balance")
    if withdrawal_amount < balance:
        balance -= withdrawal_amount
        return print(f"Withdrawal succesfull.New balance is {balance}")


def checkbalance():
    global balance
    return print((f"Your balance is {balance}"))


def main():
    while True:
        choice= input(f"Kindly enter your choice : ")
        if choice==("1"):
            deposit()
        elif choice==("2"):
            withdrawal()
        elif choice==("3"):
            checkbalance()
        else :
            print("Exiting from app")
            break

main()
