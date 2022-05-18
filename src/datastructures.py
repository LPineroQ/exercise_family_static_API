from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [{
            "id": self._generateId(),
            "first_name": "John"
            "last_name": self.last_name
            "age": 33
            "lucky_numbers": [7, 13, 22]
        },
        {
           "id": self._generateId(),
            "first_name": "Jane"
            "last_name": self.last_name
            "age": 35
            "lucky_numbers": [10, 14, 3] 
        }, 
        {"id": self._generateId(),
            "first_name": "Jimmy"
            "last_name": self.last_name
            "age": 5
            "lucky_numbers": [1]
        }]

    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        if member["id"] is None:
            member["id"]= self._generateId()
        if member:
            self._members.append(member)
            return True
        else:
            return False

    def delete_member(self, id):
        for i, member in enumerate(self._members, start=0):
            if member["id"] == int(id):
                self._members.pop(i)
                return {"done": True}
        return None

    def get_member(self, id):
        for member in self._members:
            if member["id"] == int(id):
                return member
        return {"id": "", "first_name": "", "age": "", "lucky_numbers": [] }

    def get_all_members(self):
        return self._members
