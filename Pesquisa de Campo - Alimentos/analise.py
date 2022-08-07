__author__ = "Grupo 05 - Macro"
__version__ = "1.0"
__status__ = "Finished"
__license__ = "https://github.com/Super-Macro/Analise-Dados-Pesquisas/blob/main/LICENSE"


## Bibliotecas necessárias
import pandas as pd

## Local do arquivo
caminho = "C:/Users/guui_/Desktop/Nova pasta/Pesquisa.xlsx"

## Arquivos salvo na variável
arq = pd.read_excel(caminho)


arq.columns     ## Colunas


## Funções Auxiliares:

def analise_comparacao(nome_coluna: str, comparacao: str) -> None:
    r"Faz a comparação dos dados em relação a uma coluna, mostrando os dados em que os valores de ```comparação``` é igual a ```sim```." 
    values = arq[nome_coluna].unique()
    
    for value in values:
        aux: pd.DataFrame = arq.loc[(arq[nome_coluna] == f'{value}')].reset_index() .drop(columns=['index'])

        ## Filtra os valores para o do 
        filtro: dict = values_count(aux[comparacao], initial_dict={"Sim":0, "Não":0})

        ## Print
        print(f"{value} -> {filtro['Sim']} pessoas (total: {sum([x for x in filtro.values()])})")


def values_count(column: list, initial_dict: dict = {}) -> dict:
    r"Faz a contagem dos valores de uma coluna"

    values = initial_dict
    for value in column:
        if value not in values:
            values[value] = 1
        else:
            values[value] += 1
    
    return values





print(f"Quantidade de pessoas em periferia: {arq['Periferia'].value_counts()}\n\n\n")

### Periferia X Renda
print("\n\nRenda das pessoas que moram em periferia")
analise_comparacao("Renda", "Periferia")


### Periferia X Ultraprocessados
print("\n\nConsumo de ultraprocessados de pessoas que moram em periferia")
analise_comparacao("Ultraprocessados", "Periferia")


### Periferia X Fast Food
print("\n\nConsumo de fast-food de pessoas que moram em periferia")
analise_comparacao("Fast-Food", "Periferia")



print(f"\n\n\nQuantidade de pessoas em Insegurança Alimentar: {arq['Insegurança Alimentar'].value_counts()}\n\n\n")

### Insegurança alimentar X Suporte
print("\n\nPessoas em insegurança alimentar que tiveram suporte")
analise_comparacao("Insegurança Alimentar - Suporte", "Insegurança Alimentar")


### Insegurança alimentar X Renda
print("\n\nRenda das pessoas em insegurança alimentar")
analise_comparacao("Renda", "Insegurança Alimentar")




### Idade X Alimentos de Qualidade
print("\n\nConsumo de alimentos de qualidade por idade:")
analise_comparacao("Idade", "AlimentosQualidade")


### Pessoas por Estado:
print(f"\n\n\nQtd de pessoas por Estado que repomderam:\n {arq['Estado'].value_counts()}\n\n\n")



### Idade X Ultraprocessados:
## print("\n\nConsumo de ultraprocessados por idade:")
## analise_comparacao("Idade", "Ultraprocessados")