from multiprocessing import Process, Manager
from flask import Flask
from flask import request
from flask import Response
from m_agent import Agent
import requests
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("num_agents", default="10", type=int)
parser.add_argument("num_req_per_agent", default="100", type=int)
args = parser.parse_args()
aggregated_agent_results = []
app = Flask(__name__)
server_results = []


@app.route("/validate_request", methods=['POST'])
def validate_json():
    content = request.get_json()
    if validate_request(content):
        server_results.append(200)
        return Response(status=200)
    else:
        server_results.append(400)
        return Response(status=400)


@app.route('/get-stats/', methods=['get'])
def visits():
    return "{}:{}:{}".format(len(server_results),
                             server_results.count(200),
                             server_results.count(400))


def validate_request(req):
    for key in req.keys():
        if key not in ["AGENT_ID", "MD5", "SHA2", "Unix_Time", "Filename", "Filepath", "File_Size", "Malicious"]:
            return False
    if "AGENT_ID" in req:
        if not isinstance(req["AGENT_ID"], str):
            return False
    else:
        return False
    if "MD5" in req:
        if not isinstance(req["MD5"], str):
            return False
    if "SHA2" in req:
        if not isinstance(req["SHA2"], str):
            return False
    else:
        return False
    if "Unix_Time" in req:
        if not isinstance(req["Unix_Time"], int):
            return False
    else:
        return False
    if "Filename" in req:
        if not isinstance(req["Filename"], str):
            return False
    else:
        return False
    if "Filepath" in req:
        if not isinstance(req["Filepath"], str):
            return False
    else:
        return False
    if "File_Size" in req:
        if not isinstance(req["File_Size"], int):
            return False
    if "Malicious" in req:
        if not isinstance(req["Malicious"], bool):
            return False

    return True


server = Process(target=app.run)
server.start()


def task(num=10):
    agent = Agent(L)
    agent.ex(num)


with Manager() as manager:
    L = manager.list()
    processes = []
    for i in range(args.num_agents):
        a = Process(target=task(args.num_req_per_agent), args=(L,))
        processes.append(a)
        a.start()

    for p in processes:
        p.join()
    print("Agent Summary")
    print("Success: {}".format(L.count(200)))
    print("Failed: {}".format(L.count(400)))
    print("Total: {}".format(len(L)))


print("Server Summary")
res = requests.get('http://localhost:5000/get-stats/')
total, success, failed = res.text.split(":")
print("Success: {}".format(success))
print("Failed: {}".format(failed))
print("Total: {}".format(total))

server.terminate()
server.join()
