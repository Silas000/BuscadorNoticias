# Busca Noticiais
Este código é um programa Python que utiliza a biblioteca `newsapi-python` para buscar notícias em tempo real sobre uma localização específica. O usuário fornece uma chave de API válida do News API, que é um serviço que oferece acesso a uma grande variedade de fontes de notícias online. O programa permite que o usuário especifique a localização desejada (cidade ou estado) e exibirá o número padrão de notícias retornadas com base na configuração gratuita da conta do News API. O número exato de notícias pode variar de acordo com a sua conta gratuita.
O número exato de notícias retornadas depende dos limites da sua conta gratuita no News API. Certifique-se de que sua chave de API seja válida e que o número de notícias retornadas esteja dentro dos limites da sua conta.

## Autores

- [@Silas Rosário](https://www.github.com/Silas000)

## Referência
 - [NewsApi](https://newsapi.org/docs)

**Campos Necessários para Funcionamento:**

1. **Chave de API do News API:** Para utilizar este programa, é necessário obter uma chave de API válida do News API. A chave de API é solicitada ao usuário no início da execução do programa.

2. **Localização (Cidade ou Estado):** O usuário deve fornecer a localização desejada para buscar notícias. Isso pode ser uma cidade específica ou um estado.


**Como Funciona:**

1. O programa começa solicitando ao usuário que insira a chave de API do News API. Sem uma chave de API válida, o programa não poderá acessar as notícias.

2. Em seguida, o programa solicita ao usuário que insira a localização desejada (cidade ou estado).

3. Com base na chave de API, localização e número de notícias fornecidos pelo usuário, o programa faz uma solicitação à API do News API para obter as notícias correspondentes.

4. As notícias são exibidas na saída padrão, incluindo informações como título, descrição, fonte e URL.



### Instalação das Bibliotecas do `requirements.txt`

1. Navegue até a pasta onde você tem o arquivo `requirements.txt` e abra um terminal ou prompt de comando.

2. Use o comando `pip` para instalar as bibliotecas listadas no `requirements.txt`. Execute o seguinte comando:

   ```bash
   pip install -r requirements.txt
   ```

   Isso instalará a biblioteca `newsapi-python` na versão especificada.

### Uso do Script `noticias.py`

1. Com as bibliotecas instaladas, você pode agora usar o script `noticias.py` para buscar notícias sobre uma localização específica.

2. Abra um terminal ou prompt de comando na mesma pasta onde você tem o arquivo `noticias.py`.

3. Execute o script `noticias.py` com o seguinte comando:

   ```bash
   python noticias.py
   ```

4. O script irá solicitar que você insira a chave de API do News API. Certifique-se de ter uma chave de API válida antes de executar o script.

5. Em seguida, o script solicitará que você insira a cidade ou estado desejado para buscar notícias.

6. O script, então, buscará notícias com base nos parâmetros fornecidos e exibirá os resultados, incluindo títulos, descrições, fontes e URLs, na saída padrão.

Lembre-se de que o número exato de notícias retornadas depende dos limites da sua conta gratuita no News API. Se você desejar personalizar a quantidade de notícias retornadas, pode fazer modificações no script `noticias.py` de acordo com suas necessidades. Certifique-se de que sua chave de API seja válida e que o número de notícias retornadas esteja dentro dos limites da sua conta.


## Screenshots

![App Screenshot](https://i.imgur.com/dZUM6Er.png)
