"""Main application file"""

from time import sleep
from flask import Flask, redirect, url_for, request
from service import my_example_service

flask_server = Flask(__name__)
service = my_example_service()


if __name__ == "__main__":
    import sys

    print("Starting server...")
    print(sys.argv)

    if len(sys.argv) > 1:

        service = my_example_service()
        if sys.argv[1] == "echo":
            print(service.echo(sys.argv))

        elif sys.argv[1] == "inverso":
            print(service.process("inverso", sys.argv[2]))

        else:
            print("XXXXX Invalid command")
