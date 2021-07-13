import argparse
from jsonToDict import FileHandler


def related_data(rooms, students):
    rel_dict = {room['id']: {'name': room['name'], 'students': []} for room in rooms}
    for student in students:
        room_for_student = rel_dict.get(student.get('room'))
        if room_for_student is not None:
            room_for_student.get('students').append(student)
    data2 = [{'id': i[0], **i[1]} for i in rel_dict.items()]
    return data2


def arg_pars():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('path1')
    parser.add_argument('path2')
    parser.add_argument('format')
    return parser


def main(path_students, path_rooms, format):
    handler = FileHandler()
    students = handler.load_data(path_students)
    rooms = handler.load_data(path_rooms)
    data_conv = related_data(rooms, students)
    if format == 'json':
        handler.export_json(data_conv)
    elif format == 'xml':
        handler.export_xml(data_conv)


if __name__ == '__main__':
    parser = arg_pars()
    args = parser.parse_args()
    main(args.path1, args.path2, args.format)
