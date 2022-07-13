from flask import Flask, jsonify, render_template, request
import json
import psycopg2

app = Flask(__name__)

'''
with app.app_context(), app.test_request_context():
    login_render = render_template("login.html")



conn = psycopg2.connect(
    host="localhost",
    database="trucos",
    user="postgres",
    password="icg28122002"
)
cur = conn.cursor()
cur.execute("select * from junio14 ORDER BY correo ASC;")
filas = cur.fetchall()
print(filas)
cur.close()
conn.close()
'''


def add_to_json_file(json_data):
    loaded_json = dict()

    with open("json_messages.json") as json_file:
        loaded_json = json.load(json_file)
        loaded_json.update(json_data)
    
    with open("json_messages.json", "w") as json_file:
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