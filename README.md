### Projeto - Análise Exploratória e PLN com a Netflix

<p align="center">
  <img src="netflix.jpg" width="640" title="hover text">
</p>

Neste projeto foram utilizados dados da Netflix obtidos em https://www.kaggle.com/datasets/shivamb/netflix-shows. Este dataset contém dados sobre o catálogo da netflix, seja filmes ou séries. Para cada filme ou série há informações sobre o elenco, diretores, ano de lançamento, descrição e etc.. A partir desses dados realizamos uma análise exploratória com pandas e as bibliotecas de visualização de dados, como matplotlib e seaborn.

Por fim, alguns conceitos básicos de Processamento de Linguagem Natural (PLN) foram aplicados para tentar obter informações sobre as descrições dos filmes e séries, separadamente, que estão listados na Netflix. O que queremos saber é: Quais são as palavras mais recorrentes nas descrições do catálogo da netflix?
Utilizamos conceitos como Bigramas, Trigramas e Quadrigramas, além de utilizar o teste-T aplicado em PLN para responder essa pergunta.

Bigramas e trigramas são termos usados na área de PLN para se referir a sequências de palavras adjacentes em um texto. A contagem da frequência de bigramas e trigramas pode ajudar a identificar padrões no texto, bem como a compreender melhor o significado das palavras em um determinado contexto. Já o teste-t é um teste estatístico usado em processamento de linguagem natural (PLN) para comparar a média de duas amostras de dados textuais.

Com a aplicação desses conceitos, conseguimos perceber que os termos New York City, World War II e Based True Story são os trigramas mais recorrentes, indicando vasta quantidade de filmes com essas temáticas. Para bigramas, destaca-se termos como Young Man e Young Woman nos primeiros lugares, o que pode indicar filmes de romance. Para séries, os bigramas mais populares são High School, Best Friend e Documentary Series. Nos dois primeiros casos temos temáticas de séries para um público mais jovem, populares na Netflix. Em terceiro lugar, o tema documentário também é bastante popular na plataforma. Já em trigramas destacamos novamente as palavras New York City e World War II.

