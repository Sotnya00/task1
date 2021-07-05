import argparse
from jsonToDict import *

def related_data(rooms, students):
    rel_dict = {room['id'] : {'name' : room['name'], 'students':[]} for room in rooms }
    for student in students:
        room_for_student = rel_dict.get(student.get('room'))
        if room_for_student is not None:
            room_for_student.get('students').append(student)
    data2 = [{'id' : i[0], **i[1]} for i in rel_dict.items()]
    return data2
