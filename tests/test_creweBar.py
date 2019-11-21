from unittest.mock import Mock
from creweBar import main


def test_main():
    name = 'test'
    data = {"name": name}
    req = Mock(get_json=Mock(return_value=data), args=data)

    result = main(req)
    assert isinstance(result, str)


class request:

    def __init__(self, json_dict: dict):
        self.json = json_dict

    def get_json(self):
        return self.json
