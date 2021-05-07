from flask import Flask, request
from colorama import init, Fore
init()

app = Flask(__name__)


#    CONFIG    #
CHAT_BUFFER = 10
MAX_MSG_LENGHT = 200
################


msgs = ["[Server started]"]


@app.route('/pull/<name>', methods=['GET'])
def pull(name):
    output = ""
    for msg in msgs:
        output = output + msg + "\n"
    output = output[:-1]
    print(Fore.CYAN + "Pull request from " + str(name) + Fore.WHITE)
    return output


@app.route('/push/<name>', methods=['POST'])
def push(name):
    content = request.json
    msg = content["msg"]
    if len(msg) <= MAX_MSG_LENGHT:
        if len(msgs) > CHAT_BUFFER:
            msgs.pop(0)
        msgs.append(name+": "+msg)
        print(Fore.GREEN + "SUCCES push from " + str(name) + Fore.WHITE)
        return "true".encode("utf8")
    else:
        print(Fore.RED + "ERROR push from " + str(name) + Fore.WHITE)
        return "false".encode("utf8")


app.run()
