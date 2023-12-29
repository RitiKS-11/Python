import pytest

from pkg.default_dict import group_by_age, protein_fruit_source


@pytest.fixture
def test_data():
    names_and_ages = [
        ("Alice", 25),
        ("Bob", 30),
        ("Charlie", 25),
        ("David", 30),
        ("Eva", 25),
        ("Frank", 30)
    ]
    return names_and_ages


@pytest.fixture
def test_data_2():
    data = [
        ("fruit", "apple"),
        ("vegetable", "carrot"),
        ("fruit", "banana"),
        ("vegetable", "spinach"),
        ("protein", "chicken"),
        ("grain", "rice"),
        ("protein", "beef"),
        ("fruit", "orange"),
        ("vegetable", "broccoli"),
        ("grain", "quinoa"),
        ("fruit", "grape"),
        ("protein", "fish"),
        ("grain", "pasta"),
        ("fruit", "strawberry"),
        ("vegetable", "tomato"),
        ("protein", "tofu"),
        ("grain", "bread"),
        ("fruit", "kiwi"),
        ("vegetable", "cucumber"),
        ("protein", "lamb"),
        ("grain", "oats"),
    ]
    return data


def test_protein_fruit_source(test_data_2):

    result = protein_fruit_source(test_data_2)
    expected_result = ['apple', 'banana', 'orange', 'grape',
                       'strawberry', 'kiwi', 'chicken', 'beef', 'fish', 'tofu', 'lamb']

    assert result == expected_result

def test_wrong_protein_fruit_source(test_data_2):
    result = protein_fruit_source(test_data_2)
    expected_result = ['apple', 'banana', 'orange', 'grape',
                       'strawberry', 'kiwi', 'chicken', 'beef', 'fish', 'tofu', 'lamb', 'carrot', 'spinach', 'broccoli', 'tomato', 'cucumber']

    
    assert result != expected_result

def test_group_by_age(test_data):
    excepted_result = {25: ['Alice', 'Charlie', 'Eva'], 30: ['Bob', 'David', 'Frank']}
    assert group_by_age(test_data) == excepted_result


if __name__ == "__main__":
    test_group_by_age([("Alice", 25),
        ("Bob", 30),
        ("Charlie", 25),
        ("David", 30),
        ("Eva", 25),
        ("Frank", 20)])