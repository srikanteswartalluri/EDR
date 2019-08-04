from multiprocessing import Process
from flask import Flask
from flask import request
from flask import Response
from m_agent import Agent

aggregated_agent_results = []
app = Flask(__name__)


@app.route("/validate_request", methods=['POST'])
def validate_json():
    content = request.get_json()
    if validate_request(content):
        return Response(status=200)
    else:
        return Response(status=400)


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return "shutting down"


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
    agent = Agent()
    agent.ex(num=num)
    agent.print_summary()
    # aggregated_agent_results += agent.get_results()


processes = []
for i in range(5):
    a = Process(target=task(100))
    processes.append(a)
    a.start()

for p in processes:
    p.join()


print("Server Summary")
# print("Success: {}".format(results.count(200)))
# print("Failed: {}".format(results.count(400)))
# print("Total: {}".format(len(results)))
# msg = r.get("msg:hello")
# print(msg)


server.terminate()
server.join()
