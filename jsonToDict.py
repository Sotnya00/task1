import json
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString

class FileHandler:
    @staticmethod
    def load_data(path):
        with open(path, 'r+', encoding = 'utf=8') as student:
            data = json.load(student)
        return data

    @staticmethod
    def export_json(data):
        with open('output.json','w') as stud_in_json:
            stud_in_json.write(json.dumps(data))

    @staticmethod
    def export_xml(data):
        out = parseString(dicttoxml(data)).toprettyxml()
        with open('output.xml', 'w') as stud_in_xml:
            stud_in_xml.write(str(out))