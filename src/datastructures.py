
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
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

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, body):
        member = {"id": self_generateId(),
        "first_name": body["first_name"],
        "last_name": self.last_name,
        "age":body["age"],
        "lucky_numbers": body["lucky_numbers"]}
        return self._members.append(member)

    def delete_member(self, id):
        member = list(filter(lambda member: member["id"] == int(id), self._members))
        if len(member)==0:
            return False
        self._members.remove(member[0])
        return self._members

    def get_member(self, id):
        member = list(filter(lambda member: member["id"] == int(id), self._members))
        if len(member)==0:
            return False 
        return member[0]

    def get_all_members(self):
        return self._members
