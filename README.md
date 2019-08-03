# EDR
Run server.py to start the server
Run agent.py to send a POST request to http://localhost:5000/validate_request  with json as below
{
    "AGENT_ID": "1",

    "MD5": "abcd12344",

    "SHA2": "sdafbasdf234r32",

    "Unix_Time": 22122018,

    "Filename": "testfile",

    "Filepath": "/path",

    "File_Size": 20,

    "Malicious": False
}

Upon receiving the request, server validates the request for the validity as per the following data types
Fields in Json Data:

AGENT ID : String (can be host name) - Compulsory 

MD5 : String - Optional

SHA2:  String - Compulsory 

Unix Time : Long -  Compulsory

Filename : String - Compulsory

Filepath : String - Compulsory 

File Size : Integer - Optional 

Malicious : Boolean - Optional
