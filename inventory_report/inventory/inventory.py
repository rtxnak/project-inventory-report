import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(self, path, type):
        list = []
        with open(path) as file:
            report = csv.DictReader(file, delimiter=",", quotechar='"')
            for row in report:
                list.append(row)
        if type == "simples":
            return SimpleReport.generate(list)
        else:
            return CompleteReport.generate(list)
