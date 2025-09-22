from xmlDataProvider import XMLReport
from adaptor import Adaptor
from report import Report


class Client:
    """
    Client class that uses the adaptor to get report data in JSON format.
    """
    def __init__(self, adaptor: Report):
        self.adaptor = adaptor

    def getReport(self):
        """
        Gets the report data in JSON format using the adaptor
        """
        return self.adaptor.getDataInJSON()

def main():
    # create an instance of XmlDataProvider
    xml_data_provider = XMLReport()
    # create an instance of Adaptor with the xml_data_provider
    adaptor = Adaptor(xml_data_provider)

    client = Client(adaptor)
    # get the report data in JSON format
    print(client.getReport())

if __name__ == "__main__":
    main()
# This is the main entry point of the application.


