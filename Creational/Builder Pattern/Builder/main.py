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

class HttpReuqestBuilder:

    def __init__(self):
        self.req = HttpRequest()
        
    def withUrl(self, url):
        self.req.url = url
        return self
    
    def withBody(self, body):
        self.req.body = body
        return self
    
    def build(self):
        return self.req
    

def main():
    httpReq = HttpReuqestBuilder().withUrl("Final").withBody("json").build()
    httpReq.execute()

if __name__ == "__main__":
    main()