from flask import Flask
from flask import request
from flask import Response


app = Flask(__name__)

results = []
@app.route("/validate_request", methods=['POST'])
def validate_json():
    content = request.get_json()
    if validate_request(content):
        results.append(200)
        return Response(status=200)
    else:
        results.append(400)
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
    if not isinstance(req["AGENT_ID"], str):
        return False
    elif not isinstance(req["MD5"], str):
        return False
    elif not isinstance(req["SHA2"], str):
        return False
    elif not isinstance(req["Unix_Time"], int):
        return False
    elif not isinstance(req["Filename"], str):
        return False
    elif not isinstance(req["Filepath"], str):
        return False
    elif not isinstance(req["File_Size"], int):
        return False
    elif not isinstance(req["Malicious"], bool):
        return False
    else:
        return True


if __name__ == '__main__':
    app.run(debug=True)
