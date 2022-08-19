from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def products_by_company(products):
        value = 0
        company_list = []

        for product in products:
            if product["nome_da_empresa"] not in company_list:
                company_list.append(product["nome_da_empresa"])

        company_dict = dict.fromkeys(company_list, value)

        for product in products:
            company_dict[product["nome_da_empresa"]] += 1

        products_by_company = ""

        for company, quantity in company_dict.items():
            products_by_company += f"- {company}: {quantity}\n"
        return products_by_company

    @classmethod
    def generate(self, products):
        simple_report = SimpleReport.generate(products)
        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{self.products_by_company(products)}"
        )
