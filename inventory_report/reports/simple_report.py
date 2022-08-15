from datetime import date, timedelta
from statistics import mode


class SimpleReport:
    def oldest_fabrication_date(products):
        current_date = date.today().strftime("%Y-%m-%d")
        oldest_fabrication_date = current_date
        for product in products:
            fabrication_date = product["data_de_fabricacao"]
            if fabrication_date < oldest_fabrication_date:
                oldest_fabrication_date = fabrication_date
        return oldest_fabrication_date

    def closest_expiration_date(products):
        current_date = date.today().strftime("%Y-%m-%d")
        closest_expiration_date = (date.today() + timedelta(days=90)).strftime(
            "%Y-%m-%d"
        )
        for product in products:
            validation_date = product["data_de_validade"]
            if (
                validation_date > current_date
                and validation_date < closest_expiration_date
            ):
                closest_expiration_date = validation_date
        return closest_expiration_date

    def company_with_the_most_products(products):
        company_with_the_most_products = mode(
            product["nome_da_empresa"] for product in products
        )
        return company_with_the_most_products

    @classmethod
    def generate(self, products):
        oldest_fabrication_date = self.oldest_fabrication_date(products)
        closest_expiration_date = self.closest_expiration_date(products)
        company_with_the_most_products = self.company_with_the_most_products(
            products
        )

        return (
            f"Data de fabricação mais antiga: {oldest_fabrication_date}\n"
            f"Data de validade mais próxima: {closest_expiration_date}\n"
            f"Empresa com mais produtos: {company_with_the_most_products}"
        )
