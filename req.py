from json import JSONEncoder
import random
import string
import time


class RequestBuilder:

    def __init__(self):
        t = int(''.join(random.choice(string.digits) for i in range(3)))
        if t % 2 != 0:
            self.AGENT_ID = self.__get_random_string()

            self.MD5 = self.__get_random_alpha_num()

            self.SHA2 = self.__get_random_alpha_num()

            self.Unix_Time = int(time.time())

            self.Filename = self.__get_random_string()

            self.Filepath = "/" + self.__get_random_string(5)

            self.File_Size = int(''.join(random.choice(string.digits) for i in range(3)))

            self.Malicious = False
        elif t % 3 != 0:
            self.AGENT_ID = self.__get_random_string()

            self.MD5 = self.__get_random_alpha_num()

            self.SHA2 = self.__get_random_alpha_num()

            self.Unix_Time = int(time.time())

            self.Filename = self.__get_random_string()

            self.Filepath = "/" + self.__get_random_string(5)

            self.File_Size = ''.join(random.choice(string.digits) for i in range(3))

            self.Malicious = False
        elif t % 5 != 0:
            self.AGENT_ID = self.__get_random_string()

            self.MD5 = self.__get_random_alpha_num()

            self.Unix_Time = int(time.time())

            self.Filename = self.__get_random_string()

            self.Filepath = "/" + self.__get_random_string(5)

            self.File_Size = int(''.join(random.choice(string.digits) for i in range(3)))

            self.Malicious = False
        else:
            self.AGENT_ID = self.__get_random_string()

            self.MD5 = self.__get_random_alpha_num()

            self.SHA2 = self.__get_random_alpha_num()

            self.Unix_Time = int(time.time())

            self.Filename = self.__get_random_string()

            self.Filepath = "/" + self.__get_random_string(5)

            self.File_Size = int(''.join(random.choice(string.digits) for i in range(3)))

            self.Malicious = False

            self.something = "extra"



    def __get_random_string(self, stringLength=8):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(stringLength))

    def __get_random_alpha_num(self,stringLength=16):
        letters_and_digits = string.ascii_letters + string.digits
        return ''.join(random.choice(letters_and_digits) for i in range(stringLength))



class RequestBuilderEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, RequestBuilder):
            return o.__dict__
        else:
            return JSONEncoder.default(self, o)
