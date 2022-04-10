"""Main application file"""

import logging
from time import sleep
from service import my_example_service

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


service = my_example_service()


if __name__ == "__main__":
    import sys

    logging.info(f"Starting server entry_shell.py with {sys.argv}")
    if len(sys.argv) > 1:

        service = my_example_service()
        if sys.argv[1] == "echo":
            logging.info(service.echo(sys.argv))

        elif sys.argv[1] == "inverso":
            logging.info(service.process("inverso", sys.argv[2]))

        else:
            logging.info(f"Invalid argument {sys.argv[1]}")

        exit(0)
    else:
        logging.error(
            f"Nenhum comamndo foi encontrado. Execute: python3 entry_shell.py <command>"
        )
