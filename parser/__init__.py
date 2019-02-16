class HttpRequest():

    method = None
    url = None

    def __init__(self, iterable):
        self.headers = {}
        self.body = None

        try: 
            self.parse_request_line(iterable)
            self.parse_headers(iterable)
            self.parse_body(iterable)
        except StopIteration as e:
            pass


    def parse_request_line(self, iterable):
        request = iterable.next().strip()
        parts = request.split(" ")

        self.method = parts[0].strip()
        self.url = parts[1].strip()

    def parse_headers(self, iterable):
        line = iterable.next().strip()

        while(not not line):
            name, value = line.split(":", 1)
            self.headers[name.strip()] = value.strip()

            line = iterable.next().strip()

    def parse_body(self, iterable):
        self.body = ""
        line = iterable.next().strip()

        while(not not line):
            self.body = self.body + "\n" + line

            line = iterable.next().strip()

    def is_valid(self):
        return self.method in ['GET', 'POST'] and \
            len(self.url) > 0

    @classmethod
    def parse_file(cls, filename):
        requests = []

        with open(filename, 'r') as fp:

            request = HttpRequest(fp)

            while(request.is_valid()):
                requests.append(request)
                request = HttpRequest(fp)


        return requests

