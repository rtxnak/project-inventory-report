import csv
import json
from xml.etree import ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def read_csv(path):
        list = []
        with open(path) as file:
            report = csv.DictReader(file, delimiter=",", quotechar='"')
            for row in report:
                list.append(row)
        return list

    def read_json(path):
        list = []
        with open(path) as file:
            content = file.read()
            list = json.loads(content)
        return list

    def read_xml(path):
        list = []
        root = ET.parse(path).getroot()
        for record in root:
            item_dict = {}
            for item in record:
                item_dict[item.tag] = item.text
            list.append(item_dict)
        return list

    def read(path):
        if path.endswith(".csv"):
            return Inventory.read_csv(path)
        elif path.endswith(".json"):
            return Inventory.read_json(path)
        elif path.endswith(".xml"):
            return Inventory.read_xml(path)

    @classmethod
    def import_data(self, path, type):
        if type == "simples":
            return SimpleReport.generate(self.read(path))
        else:
            return CompleteReport.generate(self.read(path))
