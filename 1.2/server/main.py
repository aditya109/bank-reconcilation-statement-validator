from flask import Flask, request
import json

server = Flask(__name__)


@server.route("/")
def slash_path_handler():
    return "api route / created ..."


@server.route("/input", methods=['POST'])
def input():
    target_text = request.data
    return target_text


@server.route("/output", methods=['POST'])
def output():
    return


server.run(port=5010, debug=True)
