from ATMRoomComponents.atm import ATM
from ATMRoomComponents.bankAccount import BankAccount
from ATMRoomComponents.card import Card
from ATMRoomComponents.user import User
from ATMStates.idleState import IdleState


def main():
    # 1. create atm with some notes of 2000, 500, 100
    atm = ATM(IdleState(), balance=0, twoThousandNote=2, fiveHundredNote=3, hundredNote=10)

    # 2. create user, card and bank_account entity
    bank_account = BankAccount(55555, 10000)  # balance 10k
    card = Card("4111222233334444", "1234", "12/30", "000", bank_account)
    user = User("Alice", card, bank_account)

    # 3. user will insert the card in the atm by getting the current state of atm
    print("-- Inserting card --")
    atm.getAtmState().insertCard(user.getCard(), atm)

    # 4. user will authenticate pin in current state
    print("-- Authenticating PIN (correct) --")
    atm.getAtmState().authenticatePin("1234", atm, user.getCard())

    # 5. user will select the operation
    # 6a. check balance path
    # print("-- Selecting check balance operation --")
    # atm.getAtmState().selectOperation("check balance", atm, user.getCard())
    # atm.getAtmState().checkBalance(atm, user.getCard())


    # 6b. cash withdrawal path (sufficient funds)
    print("-- Selecting withdraw operation (sufficient funds) --")
    atm.getAtmState().selectOperation("withdraw", atm, user.getCard())
    atm.getAtmState().withdrawCash(7700, atm, user.getCard())

    # 7. cash withdrawal insufficient funds case
    # print("-- Attempting withdraw with insufficient account balance --")
    # atm.getAtmState().withdrawCash(20000, atm, user.getCard())


if __name__ == '__main__':
    main()
