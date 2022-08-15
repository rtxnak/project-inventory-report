from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        1,
        "nome_do_produto",
        "nome_da_empresa",
        "12/08/2022",
        "18/09/2023",
        "111111",
        "instrucoes",
    )

    assert product.__repr__() == (
        "O produto nome_do_produto"
        " fabricado em 12/08/2022"
        " por nome_da_empresa com validade"
        " até 18/09/2023"
        " precisa ser armazenado instrucoes."
    )
