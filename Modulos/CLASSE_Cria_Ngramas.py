
import pandas as pd
import nltk


class Cria_Ngramas:
    
    def __init__(self, vetor_palavras):
        self.vetor_palavras = vetor_palavras
    
    def Bigramas(self):
        
        # Criando objetos Bigramas, Trigramas e Quadrigramas
        bigramas = nltk.collocations.BigramAssocMeasures()

        # Aplicando no vetor de palavras
        buscaBigramas = nltk.collocations.BigramCollocationFinder.from_words(self.vetor_palavras)

        # Obtendo os itens
        bigrama_freq = buscaBigramas.ngram_fd.items()

        # Tabela com Bigramas e Teste T
        FreqTabBigramas = pd.DataFrame(list(bigrama_freq),
                                       columns = ['Bigrama', 'Freq']).sort_values(by = 'Freq', ascending = False)
        
        TestetTabBigramas = pd.DataFrame(list(buscaBigramas.score_ngrams(bigramas.student_t)),
                                         columns = ['Bigrama', 'Teste-t']).sort_values(by = 'Teste-t', ascending = False)
        
        self.Tabela_Bigramas = pd.merge(FreqTabBigramas, TestetTabBigramas, on = 'Bigrama', how = 'inner')
        
        return self.Tabela_Bigramas
    
    def Trigramas(self):
        
        # Criando objetos Bigramas, Trigramas e Quadrigramas
        trigramas = nltk.collocations.TrigramAssocMeasures()

        # Aplicando no vetor de palavras
        buscaTrigramas = nltk.collocations.TrigramCollocationFinder.from_words(self.vetor_palavras)

        # Obtendo os itens
        trigrama_freq = buscaTrigramas.ngram_fd.items()

        # Tabela com Bigramas
        FreqTabTrigramas = pd.DataFrame(list(trigrama_freq),
                                        columns = ['Trigrama','Freq']).sort_values(by = 'Freq', ascending = False)
        
        TestetTabTrigramas = pd.DataFrame(list(buscaTrigramas.score_ngrams(trigramas.student_t)),
                                          columns = ['Trigrama', 'Teste-t']).sort_values(by = 'Teste-t', ascending = False)
        
        self.Tabela_Trigramas = pd.merge(FreqTabTrigramas, TestetTabTrigramas, on = 'Trigrama', how = 'inner')
        
        return self.Tabela_Trigramas
    
    def Quadrigramas(self):
        
        # Criando objetos Bigramas, Trigramas e Quadrigramas
        quadrigramas = nltk.collocations.QuadgramAssocMeasures()

        # Aplicando no vetor de palavras
        buscaQuadrigramas = nltk.collocations.QuadgramCollocationFinder.from_words(self.vetor_palavras)

        # Obtendo os itens
        quadrigrama_freq = buscaQuadrigramas.ngram_fd.items()

        # Tabela com Bigramas
        FreqTabQuadrigramas = pd.DataFrame(list(quadrigrama_freq),
                                           columns = ['Quadrigrama','Freq']).sort_values(by = 'Freq', ascending = False)
        
        TestetTabQuadrigramas = pd.DataFrame(list(buscaQuadrigramas.score_ngrams(quadrigramas.student_t)),
                                    columns = ['Quadrigrama', 'Teste-t']).sort_values(by = 'Teste-t', ascending = False)
        
        self.Tabela_Quadrigramas = pd.merge(FreqTabQuadrigramas, TestetTabQuadrigramas, on = 'Quadrigrama', how = 'inner')
        
        return self.Tabela_Quadrigramas
