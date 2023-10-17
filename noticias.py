# CRIADO POR SILAS ROSARIO
from newsapi.newsapi_client import NewsApiClient

def buscar_noticias():
    # Solicita a chave da API ao usuário
    api_key = input('Insira sua chave de API do News API: ')
    
    # Cria uma instância do NewsApiClient com a chave de API
    newsapi = NewsApiClient(api_key=api_key)
    
    # Solicita a cidade ou estado ao usuário
    localizacao = input('Insira a cidade ou estado desejado: ')
    
    # Parâmetros da consulta
    query = localizacao
    language = 'pt'  # Idioma das notícias (Português)
    
    noticias = newsapi.get_everything(q=query, language=language)
    
    # Exibe os títulos das notícias
    if 'articles' in noticias:
        for idx, noticia in enumerate(noticias['articles'], start=1):
            print(f'Notícia {idx}:')
            print(f'Título: {noticia["title"]}')
            print(f'Descrição: {noticia["description"]}')
            print(f'Fonte: {noticia["source"]["name"]}')
            print(f'URL: {noticia["url"]}')
            print('---')
    else:
        print(f'Nenhuma notícia encontrada sobre {localizacao}')

if __name__ == '__main__':
    buscar_noticias()
