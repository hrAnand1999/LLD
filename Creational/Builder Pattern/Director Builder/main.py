class HttpRequest:

    def __init__(self):
        self.url = None
        self.body = None
        self.query = None
        self.method = None

    def execute(self):
        print(f'{self.url}')
        print("-----")
        print(f'{self.body}')
        print(f"{self.query}")

class HttpReuqestBuilder:

    def __init__(self):
        self.req = HttpRequest()
        
    def withUrl(self, url):
        self.req.url = url
        return self
    
    def withBody(self, body):
        self.req.body = body
        return self
    
    def withMethod(self, method):
        self.req.method = method
        return self
    
    def withQueryParams(self, query):
        self.req.query = query
        return self
    
    def build(self):
        return self.req
    
class DirectorBuilder:

    def __init__(self):
        pass

    def getJsonRequest(self):
        return HttpReuqestBuilder().withUrl("https://api.example.com").withQueryParams('{"key": "value"}').build()
    
    def postRequest(self):
        return HttpReuqestBuilder().withUrl("https://api.example.com").withMethod("POST").withBody('{"data": "example"}').build()

def main():
    httpGetReq = DirectorBuilder().getJsonRequest()
    httpGetReq.execute()
    httpPostReq = DirectorBuilder().postRequest()
    httpPostReq.execute()

if __name__ == "__main__":
    main()