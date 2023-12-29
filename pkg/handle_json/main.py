import json

class Student:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def serialize(self):
        std = {
            'name': self.name,
            'age': self.age,
            'city':self.city
        }

        json_data = json.dumps(std, indent=4)

        return json_data

    def deserialize(self):
        json_data = self.serialize()
        return json.loads(json_data)



