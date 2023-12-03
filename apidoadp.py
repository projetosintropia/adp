import json
import sys

from flask import Flask, request, Response

app = Flask(__name__)

@app.route("/")
def index():
    return "Olá, mundo!"

@app.route("/api/v1/topics/<topic_name>", methods=["GET"])
def get_topic(topic_name):
    with open(os.path.join(os.path.dirname(__file__), "database.json")) as database:
        database_data = json.load(database)

    if topic_name in database_data:
        topic_data = database_data[topic_name]

        return Response(json.dumps(topic_data), mimetype="application/json")

    else:
        return Response(status=404)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
