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


if __name__ == "__main__":
    import sys

    print(sys.argv)

    if len(sys.argv) > 1:

        my_s = my_example_service()
        if sys.argv[1] == "echo":
            my_s.echo(sys.argv)

        elif sys.argv[1] == "inverso":
            my_s.process("inverso", sys.argv[2])

        else:
            print("Invalid command")
