import json


class my_example_service:
    def __init__(self):
        print("init")

    def echo(self, **kwargs):
        """Reverse and return the provided URI"""
        # output = {"path": path, "arg": args, "load": load}
        return json.dumps(kwargs, indent=2, sort_keys=True)

    def process(self, path, arg):
        print(f"path:{path} arg:{arg}")
        return "".join(reversed(arg))
