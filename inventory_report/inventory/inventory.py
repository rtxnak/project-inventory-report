import csv
import json
from xml.etree import ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(self, path, type):
        list = []
        if path.endswith(".csv"):
            with open(path) as file:
                report = csv.DictReader(file, delimiter=",", quotechar='"')
                for row in report:
                    list.append(row)
        if path.endswith(".json"):
            with open(path) as file:
                content = file.read()
                list = json.loads(content)
        if path.endswith(".xml"):
            root = ET.parse(path).getroot()
            for record in root:
                item_dict = {}
                for item in record:
                    item_dict[item.tag] = item.text
                list.append(item_dict)
        if type == "simples":
            return SimpleReport.generate(list)
        else:
            return CompleteReport.generate(list)
