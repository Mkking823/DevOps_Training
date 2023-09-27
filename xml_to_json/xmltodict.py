import xmltodict
import json

def xmltojson(xml_file):
    with open(xml_file, "r") as xml_file:
        xml_data = xml_file.read()
    # Convert XML to a dictionary
    xml_dict = xmltodict.parse(xml_data)
    # Convert the dictionary to JSON
    json_data = json.dumps(xml_dict, indent=2)
    print(json_data)
xml_file = input("Enter the xml_filename: ")
xmltojson(xml_file)
