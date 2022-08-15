from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def products_by_company(products):
        products_by_companies_name = {
            product["nome_da_empresa"]: 0 for product in products
        }
        for product in products:
            products_by_companies_name[product["nome_da_empresa"]] += 1
        products_by_company = ""
        for company in products_by_companies_name.items():
            products_by_company += f"- {company[0]}: {company[1]}\n"
        return products_by_company

    @classmethod
    def generate(self, products):
        simple_report = SimpleReport.generate(products)
        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{self.products_by_company(products)}"
        )
