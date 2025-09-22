from abc import  abstractmethod

class PaymentInterface:

    def __init__(self):
        pass

    @abstractmethod
    def processPayment(self):
        pass

class PaymentProcess(PaymentInterface):

    def __init__(self):
        super().__init__()

    def processPayment(self, amount):
        print(f'Processing payment of {amount}')

class LoggingDecorator(PaymentInterface):

    def __init__(self, processor):
        self.processor = processor

    def processPayment(self, amount):
        print(f'Adding Log for process amount {amount}')
        return self.processor.processPayment(amount)
    

class SecurityDecorator(PaymentInterface):

    def __init__(self, processor):
        self.processor = processor

    def processPayment(self, amount):
        print(f'Adding security for process amount {amount}')
        return self.processor.processPayment(amount)

    


def main():
    processor =  PaymentProcess()
    securityAndLog = LoggingDecorator(SecurityDecorator(processor))

    securityAndLog.processPayment(500)

if __name__ == '__main__':
    main()