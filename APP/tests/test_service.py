"""Unit test file for app.py"""
from service import my_example_service
import unittest
import json


class TestApp(unittest.TestCase):
    """Unit tests defined for app.py"""

    def setUp(self):
        self.service = my_example_service()

    # def test_my_example_service_echo(self):

    #     path = "path"
    #     args = {"arg1": "value1"}
    #     load = {
    #         "item1": [5, 5, 6, 8, 9, 1, 4, 5, 6, 6],
    #         "item2": [5, 5, 6, 8, 9, 1, 4, 5, 6, 6],
    #     }

    #     expected_output = json.dumps(
    #         {"path": path, "arg": args, "load": load}, indent=2, sort_keys=True
    #     )

    #     real_output = self.service.echo({"path": path, "arg": args, "load": load})
    #     self.assertEqual(expected_output, real_output)

    def test_my_example_service_inverso(self):

        path = "path"
        arg = "jennifer"
        load = None
        expected_output = "refinnej"

        real_output = self.service.process(path, arg, load)
        self.assertEqual(expected_output, real_output)


if __name__ == "__main__":
    unittest.main()
