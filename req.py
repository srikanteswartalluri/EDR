from json import JSONEncoder


class RequestBuilder:
    def __init__(self):
        self.AGENT_ID = "1"

        self.MD5 = "abcd12344"

        self.SHA2 = "sdafbasdf234r32"

        self.Unix_Time = 22122018

        self.Filename = "testfile"

        self.Filepath = "/path"

        self.File_Size = 20

        self.Malicious = False

    def get_invalid_request(self):
        self.AGENT_ID = "1"

        self.MD5 = "abcd12344"

        self.SHA2 = "sdafbasdf234r32"

        self.Unix_Time = 22122018

        self.Filename = "testfile"

        self.Filepath = "/path"

        self.File_Size = "20"

        self.Malicious = False

        return self



class RequestBuilderEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, RequestBuilder):
            return o.__dict__
        else:
            return JSONEncoder.default(self, o)
