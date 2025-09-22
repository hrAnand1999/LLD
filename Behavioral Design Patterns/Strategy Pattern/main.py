from paymentClass import PaymentStrategy
from upi import UPI
from netbanking import NetBanking
from creditCard import CreditCard

def main():
    upi = UPI()
    creditCard = CreditCard()
    netBanking = NetBanking()

    payment = PaymentStrategy(upi)
    payment.pay(200)

    payment.setStrategy(creditCard)
    payment.pay(300)

    payment.setStrategy(netBanking)
    payment.pay(400)


if __name__ == "__main__":
    main()