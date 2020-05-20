from bs4 import BeautifulSoup

def get_dtpinfra_token(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        DTPINFRA_TOKEN = soup.find("input",
                                   {"name": "DTPINFRA_TOKEN"}).get(
                'value')

        if not DTPINFRA_TOKEN:
            raise Exception("Erro ao obter DTPINFRA_TOKEN")

        return DTPINFRA_TOKEN
    except:
        raise Exception("Erro ao obter DTPINFRA_TOKEN")


