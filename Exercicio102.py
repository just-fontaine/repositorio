import requests


def check_site(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f'Consegui acessar o site {url} com sucesso.')
        else:
            print(f'Erro ao acessar o site {url}. Código de status: {response.status_code}')
    except requests.ConnectionError:
        print(f'O site {url} não está acessível no momento.')
    except Exception as e:
        print(f'Ocorreu um erro ao acessar {url}: {e}')


check_site('https://www.pudim.com.br')
check_site('http://www.google.com')
