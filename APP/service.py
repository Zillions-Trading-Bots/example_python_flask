import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class my_example_service:
    def __init__(self):
        logging.info("my_example_service.__init__()")

    def echo(self, **kwargs):
        logging.info(f"my_example_service.echo({kwargs})")
        """Reverse and return the provided URI"""
        return json.dumps(kwargs, indent=2, sort_keys=True)

    def process(self, path, arg):
        logging.info(f"my_example_service.process({path}, {arg})")
        return "".join(reversed(arg))
