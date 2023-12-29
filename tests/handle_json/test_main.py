import pytest
import json

from pkg.handle_json.main import Student

@pytest.fixture
def std():
    return Student("Ritik", 25, "kathmandu")

def test_serialize(std):
    expected_result = json.dumps({"name": "Ritik","age": 25,"city": "kathmandu"}, indent=4)
    assert std.serialize() == expected_result


def test_deserialize(std):
    expected_result = {"name": "Ritik","age": 25,"city": "kathmandu"}
    assert std.deserialize() == expected_result


if __name__ == "__main__":
    test_deserialize(Student("Ritik", 25, "kathmandu"))
    test_serialize(Student("Ritik", 25, "kathmandu"))
