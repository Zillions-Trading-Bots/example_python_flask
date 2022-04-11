"""Main application file"""

import logging
import sys
from time import sleep
from flask import Flask, redirect, url_for, request
from service import my_example_service
import sys

flask_server = Flask(__name__)
service = my_example_service()

# logging.basicConfig(stream=sys.stdout, level=logging.INFO)


@flask_server.route("/<random_string>", methods=["GET", "POST"])
def random_path(random_string):

    logging.info(f"Route <random_string>  with random_string:{random_string}")
    load = None

    method = request.method
    content_type = request.content_type

    if method == "POST":
        if request.data:
            if content_type == "application/json":
                load = request.get_json(silent=False)
            elif content_type == "application/x-www-form-urlencoded":
                load = request.form.to_dict()
            elif content_type == "text/plain":
                load = request.data.decode("utf-8")
            else:
                load = request.get_data()

    # if key doesn't exist, returns None
    args = request.args.to_dict()

    return service.echo(
        path=random_string,
        method=method,
        content_type=content_type,
        args=args,
        load=load,
    )


@flask_server.route("/inverso", methods=["GET"])
def process():

    logging.info(f"Route /inversor")
    # if key doesn't exist, returns None
    arg1 = request.args.get("palavra", "None")

    return service.process("inversor", arg1)


@flask_server.route("/", methods=["GET"])
def root():
    logging.info(f"Route /")
    return "Root! Up and Running!"


@flask_server.route("/health", methods=["GET"])
def health():
    logging.info(f"Route /health")
    return "Health and Running!"


if __name__ == "__main__":
    logging.info(f"Starting server entry_flask.py:__main__")
    flask_server.run(host="0.0.0.0", port=5000)
