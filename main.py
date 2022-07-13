from flask import Flask, request
import json

app = Flask(__name__)

file_path = "json_messages.json"

def add_to_json_file(json_data):
    loaded_json = dict()

    with open(file_path) as json_file:
        loaded_json = json.load(json_file)
        loaded_json.update(json_data)
    
    with open(file_path, "w") as json_file:
        json.dump(loaded_json, json_file)

    return {"status": "ok"}

def get_messages_by_topic(t):
    loaded_json = dict()
    with open("json_messages.json") as json_file:
        loaded_json = json.load(json_file)

    query = dict()
    for message, topic in loaded_json.items():
        print(topic, t)
        if topic == t:
            query[message] = topic

    return query

@app.route("/message",methods=["POST"])
def login_post():
    json = request.get_json()

    return add_to_json_file(json)

@app.route("/message",methods=["GET"])
def login_get():
    topic = request.args

    return get_messages_by_topic(list(topic.keys())[0])
        

app.run(port=8080, debug=True)