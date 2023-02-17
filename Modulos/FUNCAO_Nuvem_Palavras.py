
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def nuvem_palavras(x):
    
    wordcloud = WordCloud(width = 1920, height = 1600, max_words = 200,
                          background_color = None, mode = 'RGBA', colormap = 'viridis',
                          relative_scaling = 'auto').generate_from_frequencies(frequencies = x)
    
    plt.figure(figsize=(14,8))
    plt.imshow(wordcloud, interpolation = 'bilinear')
    plt.axis('off')
    plt.show();


