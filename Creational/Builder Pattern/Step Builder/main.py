from abc import abstractmethod

class HttpRequest:

    def __init__(self):
        self.url = None
        self.body = None
        self.query = None
        self.method = None

    def execute(self):
        print(f'{self.url}')
        print(f'{self.method}')
        print("-----")
        if self.query:
            print(f'Query: {self.query}')
        if self.body:
            print(f'Body: {self.body}')

class Url:

    def __init__(self, req):
        self.req = req
    
    # @abstractmethod
    def withUrl(self, url: str):
        self.req.url = url
        return Method(self.req)

class Method:

    def __init__(self, req):
        self.req = req
    
    # @abstractmethod
    def withMethod(self, method: str):
        self.req.method = method
        return Optional(self.req)

class Optional:

    def __init__(self, req):
        self.req = req
    
    # @abstractmethod
    def withQuery(self, query: str):
        self.req.query = query
        return self

    # @abstractmethod
    def withBody(self, body: str):
        self.req.body = body
        return self
    
    def build(self):
        return self.req

class StepBuilder():

    def __init__(self):
        self.req = HttpRequest()

    def start(self):
        return Url(self.req)
 
def main():
    req = StepBuilder().start() \
                       .withUrl("https://example.com") \
                       .withMethod("POST") \
                       .withQuery("id=123") \
                       .build()
    
    req.execute()

if __name__ == "__main__":
    main()