from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        "nome_do_produto",
        "nome_da_empresa",
        "12/08/2022",
        "18/09/2023",
        "111111",
        "instrucoes",
    )

    assert product.id is int(1)
    assert product.nome_do_produto is str("nome_do_produto")
    assert product.nome_da_empresa is str("nome_da_empresa")
    assert product.data_de_fabricacao is str("12/08/2022")
    assert product.data_de_validade is str("18/09/2023")
    assert product.numero_de_serie is str("111111")
    assert product.instrucoes_de_armazenamento is str("instrucoes")
