
from nltk.tokenize import sent_tokenize
from nltk.tokenize import TreebankWordTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
import spacy



def bag_words(dataframe, coluna):
    
    # Fazendo copia do dataframme
    df = dataframe.copy()
    
    # Filtrando para coluna desejada
    df = df[df['type'] == coluna]
    
    # Colocando as palavras em letras minúsculas, passando para uma lista e no fim colocando em modo str
    df['description'] = df['description'].str.lower()
    palavras = df['description']
    palavras = palavras.astype(str)
    
    # Criando o objeto que vai aplicar o tokenizer para palavras em inglês e aplicando
    tokenizer = TreebankWordTokenizer()
    english_stops = set(stopwords.words('english'))
    palavras = [tokenizer.tokenize(palavra) for palavra in palavras]
    
    # Obtendo as palavras em uma só lista
    palavras = [i for palavra in palavras for i in palavra]
    
    # Eliminando stopwords
    palavras = [palavra for palavra in palavras if palavra not in english_stops]
    
    # Mais uma etapa de remoção de caracteres indesejáveis
    lista_remove = ["-", "—",",", ".", "'", "`", "´", "~", "^", "'s", "'t", "``", '"', "–", "$", "!"]
    palavras = [palavra for palavra in palavras if palavra not in lista_remove]
    
    # Criando o objeto que vai aplicar o lemmatizer e aplicando
    wordnet_lemmatizer = WordNetLemmatizer()
    palavras = [wordnet_lemmatizer.lemmatize(i) for i in palavras]
    
    return palavras