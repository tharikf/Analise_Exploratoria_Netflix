
from collections import Counter

def conta_palavras(dataframe, coluna):
    
    df = dataframe.copy()
    
    # Dropando NA
    df = df.dropna(subset = [coluna])
    
    # Corrigindo coluna
    df[coluna] = df[coluna].str.replace(', ', ',')
    
    # Obtendo o cast de cada filme em formato de lista
    lista_contado = [i.split(',') for i in df[coluna]]
    
    # Para cada cast em lista, obter os nomes dos atores separadamente
    total_contado = [i for sublista in lista_contado for i in sublista]
    
    # Contar a quantidade de atores
    contagem = Counter(total_contado)
    
    # Retorna os 10 principais
    return contagem

